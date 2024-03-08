import winreg
import ctypes
import sys

# 관리자 권한으로 실행
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def set_processor_name(name):
    try:
        # 레지스트리 키 열기
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0", 0, winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE)

        # ProcessorNameString의 현재 값 가져오기
        current_value, _ = winreg.QueryValueEx(key, "ProcessorNameString")
        print("현재 CPU 이름 :", current_value)

        # ProcessorNameString에 새로운 값 설정
        winreg.SetValueEx(key, "ProcessorNameString", 0, winreg.REG_SZ, name)

        # 레지스트리 키 닫기
        winreg.CloseKey(key)
        print("CPU 이름이 {} 으로 성공적으로 변경되었습니다.".format(name))
    except Exception as e:
        print("오류가 발생했습니다:", e)

def main():
    if is_admin():
        # 사용자로부터 새 프로세서 이름 입력 또는 기본값 설정
        user_input = input("새 프로세서 이름을 입력해주세요. 입력하지 않으면 기본값으로 설정됩니다.\n(기본값: Intel(R) Core(TM) i9-13900x cpu @ 3.70ghz): ")
        new_processor_name = user_input if user_input else "Intel(R) Core(TM) i9-13900x cpu @ 3.70ghz"
        
        # 새 프로세서 이름 설정 함수 호출
        set_processor_name(new_processor_name)
    else:
        # 현재 스크립트를 다시 관리자 권한으로 실행
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

if __name__ == "__main__":
    main()
