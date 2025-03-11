# config.spec
block_cipher = None

a = Analysis(['GUIPage.py'],
             pathex=['D:\\thing\\DIAD\\final\\DIAD\\GUI'],
             binaries=[],
             datas=[('D:\\thing\\DIAD\\final\\DIAD\\SDGUI','SDGUI')],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             hiddenimports=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='DIAD',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)
