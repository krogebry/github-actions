
auto-doc action:
    @echo "{{ action }}"
    ./bin/auto-doc.py {{ action }}

auto-doc-all:
   for dir in `find ./ -name "action.yaml" -exec dirname {} \;`; do just auto-doc $dir; done
