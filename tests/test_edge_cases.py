import pytest
import sys
from httpie.core import main
from httpie.status import ExitStatus

def test_main_with_invalid_arguments(capsys):
    """
    Master's Project - Advanced Software Verification.
    Test how the HTTPie core bootstrap main() function handles 
    unexpected terminal argument configurations cleanly under isolations.
    """
    # عزل البيئة تماماً وتمرير قائمة وسائط نقية لا تتأثر بـ pytest
    # سنمرر دالة الاستدعاء مع علم خاطئ بشكل صريح
    test_args = ['http', '--invalid-flag-for-testing']
    
    # حفظ النسخة الأصلية من وسائط النظام
    original_argv = sys.argv
    
    try:
        # استبدال كامل لمصفوفة وسائط النظام لعزل دالة main
        sys.argv = test_args
        
        # استدعاء الدالة والتقاط القيمة الراجعة (Exit Status)
        exit_status = main()
        
        # التحقق من أن النظام تعامل مع الخطأ بذكاء ولم يهنق، بل أرجع كود خطأ
        assert exit_status == ExitStatus.ERROR
        
    except SystemExit as e:
        # في حال قامت مكتبة argparse بقطع التنفيذ والخروج المباشر
        assert e.code in [ExitStatus.ERROR, 2]
        
    finally:
        # إعادة النظام لحالته الأصلية فوراً بعد الفحص لعدم تخريب الفحوصات الأخرى
        sys.argv = original_argv