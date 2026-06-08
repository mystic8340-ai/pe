import importlib
mods=['streamlit','pandas','numpy','joblib','sklearn','scikeras','tensorflow','keras']
for m in mods:
    try:
        importlib.import_module(m)
        print(m+': OK')
    except Exception as e:
        print(m+': ERROR: '+repr(e))
