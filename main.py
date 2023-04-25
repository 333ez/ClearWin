## módulos
import ctypes
import os
import shutil
import subprocess
import sys

## verifica se o programa está sendo executado como admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clear_event_logs():
    for line in os.popen('wevtutil.exe el'):
        if line.strip():
            os.system(f'wevtutil.exe cl "{line.strip()}"')

os.system('cls')
print('\n')
print('DIGITE O NUMERO DA OPCAO DESEJADA\n')
print('[1] Limpar arquivos Temporarios')
print('[2] Finalizar Execucoes')
print('[3] Executar Limpeza Profunda (Requer Administrador)')
print('[4] Desativar Atualizacoes do Windows')
print('[5] sair')

opcao = input('\nDigite a opcao Desejada: ')

## executa o cleanmgr.exe para limpar os arquivos temporários
if opcao == '1':
    os.system('cleanmgr.exe /dCnidade')
## para o serviço SDRSVC
elif opcao == '2':
    os.system('net stop SDRSVC')
## executa uma limpeza profunda do sistema
elif opcao == '3':
    if not is_admin():
        print('Sem permissao de administrador.')
        sys.exit(1)
    os.system('color a')
    os.system('del /s /f /q C:\\WINDOWS\\Prefetch\\*.*')
    os.system('del /s /f /q %temp%\\*.*')
    os.system('del c:\WIN386.SWP')
    os.system('rd /y c:\windows\cookies')
    os.system('rd /y c:\windows\spool\printers')
    os.system('rd /y c:\windows\recent')
    os.system('rd /y c:\windows\history')
    os.system('rd /y c:\windows\ff*.tmp')
    os.system('rd /y c:\windows\tempor~1')
    shutil.rmtree(os.environ['TEMP'], ignore_errors=True)
    os.mkdir(os.environ['TEMP'])
    clear_event_logs()
## para o serviço wuauserv
elif opcao == '4':
    os.system('net stop wuauserv')
## finaliza o programa
elif opcao == '5':
    print('\nSaindo...')
    sys.exit(0)
else:
    print('\nOpcao invalida!')
    sys.exit(1)

print('\nOperacao executada com sucesso!')
input('\nPressione qualquer tecla para encerrar...')