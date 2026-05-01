import json
import os
import pytest
from pathlib import Path
from .utils import http, MockEnvironment, HTTP_OK


class TestSaveMeta:
    def test_save_meta_creates_valid_json(self, tmp_path, httpbin):
        meta_file = tmp_path / 'meta.json'
        r = http(
            '--save-meta', str(meta_file),
            'GET', httpbin + '/get',
            'test-header:foo'
        )
        assert HTTP_OK in r
        assert meta_file.exists()
        
        with open(meta_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert isinstance(data, list)
        assert len(data) == 1
        
        record = data[0]
        assert 'timestamp' in record
        assert 'request' in record
        assert 'response' in record

    def test_save_meta_request_fields_complete(self, tmp_path, httpbin):
        meta_file = tmp_path / 'meta.json'
        r = http(
            '--save-meta', str(meta_file),
            'POST', httpbin + '/post',
            'Custom-Header:test-value',
            'foo=bar',
            'baz:=123'
        )
        assert HTTP_OK in r
        
        with open(meta_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        record = data[0]
        request = record['request']
        
        assert request['method'] == 'POST'
        assert httpbin + '/post' in request['url']
        assert 'headers' in request
        assert isinstance(request['headers'], dict)
        
        assert 'body' in request
        assert 'foo' in request['body']
        assert 'bar' in request['body']
        assert 'baz' in request['body']
        assert '123' in request['body']
        
        assert 'Custom-Header' in request['headers'] or 'custom-header' in request['headers']

    def test_save_meta_response_fields_complete(self, tmp_path, httpbin):
        meta_file = tmp_path / 'meta.json'
        r = http(
            '--save-meta', str(meta_file),
            'GET', httpbin + '/get?foo=bar'
        )
        assert HTTP_OK in r
        
        with open(meta_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        record = data[0]
        response = record['response']
        
        assert response['status_code'] == 200
        assert 'headers' in response
        assert isinstance(response['headers'], dict)
        assert 'body_preview' in response
        assert 'total_time_seconds' in response
        assert isinstance(response['total_time_seconds'], (int, float))
        assert response['total_time_seconds'] >= 0

    def test_save_meta_appends_to_existing_file(self, tmp_path, httpbin):
        meta_file = tmp_path / 'meta.json'
        
        for i in range(3):
            r = http(
                '--save-meta', str(meta_file),
                'GET', httpbin + f'/get?id={i}'
            )
            assert HTTP_OK in r
        
        with open(meta_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert isinstance(data, list)
        assert len(data) == 3
        
        for i, record in enumerate(data):
            assert f'id={i}' in record['request']['url']

    def test_save_meta_with_output_option(self, tmp_path, httpbin):
        meta_file = tmp_path / 'meta.json'
        output_file = tmp_path / 'output.txt'
        
        r = http(
            '--save-meta', str(meta_file),
            '--output', str(output_file),
            'GET', httpbin + '/robots.txt'
        )
        
        assert meta_file.exists()
        assert output_file.exists()
        
        with open(meta_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert len(data) == 1
        assert data[0]['response']['status_code'] == 200
        
        output_content = output_file.read_text(encoding='utf-8')
        assert 'User-agent' in output_content

    def test_save_meta_with_body_preview(self, tmp_path, httpbin):
        meta_file = tmp_path / 'meta.json'
        long_body = 'x' * 2000
        
        r = http(
            '--save-meta', str(meta_file),
            '--raw', long_body,
            'POST', httpbin + '/post'
        )
        assert HTTP_OK in r
        
        with open(meta_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        record = data[0]
        response = record['response']
        
        assert 'body_preview' in response
        assert len(response['body_preview']) <= 1024

    def test_save_meta_offline_mode(self, tmp_path):
        meta_file = tmp_path / 'meta.json'
        
        r = http(
            '--save-meta', str(meta_file),
            '--offline',
            'POST', 'http://example.org/test',
            'Content-Type:application/json',
            'foo=bar'
        )
        
        assert meta_file.exists()
        
        with open(meta_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert len(data) == 1
        record = data[0]
        
        assert 'request' in record
        assert record['request']['method'] == 'POST'
        assert 'example.org' in record['request']['url']
        assert 'body' in record['request']
        
        assert 'response' not in record

    def test_save_meta_with_invalid_existing_file(self, tmp_path, httpbin):
        meta_file = tmp_path / 'meta.json'
        
        meta_file.write_text('this is not valid json', encoding='utf-8')
        
        r = http(
            '--save-meta', str(meta_file),
            'GET', httpbin + '/get'
        )
        assert HTTP_OK in r
        
        with open(meta_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        assert isinstance(data, list)
        assert len(data) == 1
