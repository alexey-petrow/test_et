import importlib
import inspect
import os
from pathlib import Path

from django.shortcuts import render
from django.views.generic import TemplateView

from config.settings import MODULES_DIR_NAME, MODULES_DIR, ALLOWED_MODULE_EXTENSIONS


def _get_modules_list(path_to_modules_dir: Path,
                      allowed_extensions: list[str]) -> list[str]:
    """
    Searches for all files in the directory and selects from them those that fit the extension.
    Args:
        path_to_modules_dir: (Path) Path to the directory with files.
        allowed_extensions: (list[str]) Allowed file extensions.
    Returns:
        (list[str]) List of file names without extension.
    """
    modules_list = []
    all_files: list[str] = os.listdir(path_to_modules_dir)
    for file_name in all_files:
        file_data = file_name.split('.')
        if file_data[-1] in allowed_extensions:
            modules_list.append(file_data[0])
    return modules_list


def _get_functions_data(modules: list[str]) -> list[dict]:
    functions_data = []
    for module_name in modules:
        try:
            module = importlib.import_module(f'{MODULES_DIR_NAME}.{module_name}')
            for name, func in inspect.getmembers(module, inspect.isfunction):
                if name.startswith(('_', '__')):
                    continue
                functions_data.append({
                    'module': module_name,
                    'name': name,
                    'docstring': inspect.getdoc(func),
                    'code': inspect.getsource(func),
                })
        except ImportError:
            pass
    return functions_data


class FunctionsTableView(TemplateView):
    template_name = 'functions_table.html'
    extra_context = {'title': 'Available Functions'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        module_names: list[str] = _get_modules_list(
            path_to_modules_dir=MODULES_DIR,
            allowed_extensions=ALLOWED_MODULE_EXTENSIONS,
        )
        functions_data: list[dict] = _get_functions_data(module_names)
        context_data['functions'] = functions_data
        return context_data
