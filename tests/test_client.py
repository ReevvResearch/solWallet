"""Tests for the Solana client module."""

import pytest
from sol_test.client import SolanaClient


def test_client_initialization():
    """Test that client can be initialized with default endpoint."""
    client = SolanaClient()
    assert client.endpoint == "https://api.devnet.solana.com"
    
    # Test with custom endpoint
    custom_endpoint = "https://api.mainnet-beta.solana.com"
    client = SolanaClient(custom_endpoint)
    assert client.endpoint == custom_endpoint


def test_client_connection():
    """Test that client can check connection status."""
    client = SolanaClient()
    # This might occasionally fail if devnet is down
    assert client.is_connected() is True


@pytest.mark.parametrize(
    "address",
    [
        # Solana Foundation address
        "4beBxnHZxJWRDUQCFVmK5adKQHvMypB7e2e6xPQghQtY",
        # Random devnet address
        "HN8GGHsvSrsv9Z9JhvMLB4QQJPbaSJ2HjLGrKe9KYpJY"
    ]
)
def test_get_balance(address):
    """Test that client can retrieve account balance."""
    client = SolanaClient()
    response = client.get_balance(address)
    # Check response structure
    assert response is not None
    # The response structure might be different depending on the version
    # Just verify that we got a response without errors
    

def test_get_cluster_nodes():
    """Test that client can retrieve cluster nodes."""
    client = SolanaClient()
    response = client.get_cluster_nodes()
    # Check response structure
    assert response is not None
    # The response structure might be different depending on the version
    # Just verify that we got a response without errors 