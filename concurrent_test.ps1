# 确保当前目录是项目根目录，虚拟环境已激活
$exe = "$PWD\.venv\Scripts\http.exe"
Remove-Item meta.json -ErrorAction SilentlyContinue
$jobs = @()
for ($i=1; $i -le 20; $i++) {
    $script = { & $using:exe --save-meta meta.json GET http://httpbin.org/get }
    $jobs += Start-Job -ScriptBlock $script
}
$jobs | Wait-Job | Out-Null
$jobs | Remove-Job

# 验证 JSON 完整性
try {
    $data = Get-Content meta.json -Raw | ConvertFrom-Json
    Write-Host "成功读取 JSON，共有 $($data.Count) 条记录"
    if ($data.Count -ne 20) { Write-Host "错误：记录数应为 20，实际为 $($data.Count)" }
} catch {
    Write-Host "JSON 损坏或无效：$_"
}