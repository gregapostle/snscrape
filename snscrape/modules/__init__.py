import pkgutil


__all__ = []


def _import_modules():
    import importlib
    import importlib.util
    import pkgutil

    for finder, moduleName, ispkg in pkgutil.iter_modules(__path__):
        spec = importlib.util.find_spec(f'{__name__}.{moduleName}')
        if spec is None:
            continue
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        globals()[moduleName] = module


_import_modules()
