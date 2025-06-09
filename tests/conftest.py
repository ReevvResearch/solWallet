"""Pytest configuration and fixtures."""

import pytest
from solders.keypair import Keypair
from solana.rpc.api import Client
from sol_test.client import SolanaClient


@pytest.fixture(scope="session")
def devnet_endpoint():
    """Return the Solana devnet RPC endpoint."""
    return "https://api.devnet.solana.com"


@pytest.fixture(scope="session")
def solana_client(devnet_endpoint):
    """Return a Solana RPC client connected to devnet."""
    return SolanaClient(devnet_endpoint)


@pytest.fixture(scope="function")
def random_keypair():
    """Return a new random keypair for each test that uses it."""
    return Keypair()


@pytest.fixture(scope="session")
def fixed_keypair():
    """Return a fixed keypair that can be used across tests."""
    # Using a fixed seed for deterministic tests
    # Note: Do not use this keypair for any real transactions
    seed_bytes = bytes([i for i in range(32)] + [i for i in range(32)])
    return Keypair.from_bytes(seed_bytes) 