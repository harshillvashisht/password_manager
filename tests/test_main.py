"""Tests for password-strength behavior in the CLI."""

from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from password_manager.main import app
from password_manager.vault import UnlockedVault


def test_add_warns_before_accepting_a_weak_password(
    tmp_path: Path,
) -> None:
    vault_path = tmp_path / "vault.json"
    runner = CliRunner()
    UnlockedVault.create(vault_path, "correct horse battery staple")

    with patch("password_manager.main._prompt_master_password", side_effect=[
        "correct horse battery staple",
        "password",
    ]), patch("builtins.input", side_effect=["alice", "", ""]), patch(
        "password_manager.main.typer.confirm",
        return_value = False,
    ):
        result = runner.invoke(
            app,
            ["add", "example", "--vault", str(vault_path)],
        )

    assert result.exit_code == 1
    assert "weak" in result.output.lower()
    with UnlockedVault.unlock(vault_path, "correct horse battery staple") as vault:
        assert vault.names() == []
