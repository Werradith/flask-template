:: DB autoupgrade script for Windows
:: Needs <python_dir>\Scripts in %PATH%
@echo off
cd /d %~dp0
alembic revision --autogenerate
alembic upgrade head