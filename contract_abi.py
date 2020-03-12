abi = """[
	{
		"constant": true,
		"inputs": [
			{
				"name": "_publisher",
				"type": "address"
			}
		],
		"name": "get_pubkey",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_publisher",
				"type": "address"
			}
		],
		"name": "isApproved",
		"outputs": [
			{
				"name": "approved",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_publisher",
				"type": "address"
			}
		],
		"name": "ApprovePublisher",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_publickey",
				"type": "string"
			},
			{
				"name": "_publisher",
				"type": "address"
			}
		],
		"name": "broadcastPublicKey",
		"outputs": [
			{
				"name": "success",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"payable": true,
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_publisher",
				"type": "address"
			},
			{
				"indexed": false,
				"name": "_publickey",
				"type": "string"
			}
		],
		"name": "PublicKeyPublish",
		"type": "event"
	}
]"""