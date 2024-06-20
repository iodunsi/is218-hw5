import pytest
from app import App

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    # Simulate user entering 'menu'
    inputs = iter(['menu'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()    

    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "- add" in out
    assert "- subtract" in out
    assert "- multiply" in out
    assert "- divide" in out
    assert "- menu" in out

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    # Simulate user entering 'add' and then two numbers
    inputs = iter(['10', '20'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()    

    app.command_handler.execute_command('add')

    out, err = capfd.readouterr()
    assert "The result is: 30.0" in out

def test_app_subtract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command."""
    # Simulate user entering 'subtract' and then two numbers
    inputs = iter(['30', '20'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()    

    app.command_handler.execute_command('subtract')

    out, err = capfd.readouterr()
    assert "The result is: 10.0" in out

def test_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multiply' command."""
    # Simulate user entering 'multiply' and then two numbers
    inputs = iter(['3', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()    

    app.command_handler.execute_command('multiply')

    out, err = capfd.readouterr()
    assert "The result is: 12.0" in out

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'divide' command."""
    # Simulate user entering 'divide' and then two numbers
    inputs = iter(['20', '5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()    

    app.command_handler.execute_command('divide')

    out, err = capfd.readouterr()
    assert "The result is: 4.0" in out

def test_app_divide_by_zero_command(capfd, monkeypatch):
    """Test that the REPL correctly handles division by zero."""
    # Simulate user entering 'divide' and then a number and zero
    inputs = iter(['20', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()    

    app.command_handler.execute_command('divide')

    out, err = capfd.readouterr()
    assert "Division by Zero isn't permitted." in out

def test_app_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command."""
    # Simulate user entering an unknown command
    inputs = iter(['unknown_command'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()    

    app.command_handler.execute_command('unknown_command')

    out, err = capfd.readouterr()
    assert "No such command: unknown_command" in out
