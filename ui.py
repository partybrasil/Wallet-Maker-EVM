from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import sys
from web3 import Web3
from eth_account import Account


class WalletApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(WalletApp, self).__init__()
        uic.loadUi('wallet_app.ui', self)

        # Conectar el botón de generación de carteras
        self.generateButton.clicked.connect(self.generate_wallets)

        # Habilitar las características no auditadas de mnemonics
        Account.enable_unaudited_hdwallet_features()

    def generate_wallets(self):
        num_wallets = self.walletCountSpinBox.value()
        if num_wallets > 10:
            QMessageBox.warning(self, "Error", "El máximo de carteras a generar es 10.")
            return

        for _ in range(num_wallets):
            self.create_wallet()

        QMessageBox.information(self, "Éxito", f"{num_wallets} carteras generadas exitosamente.")

    def create_wallet(self):
        # Generar una nueva cuenta
        account = Account.create()

        # Generar una frase mnemónica
        address, mnemonic = Account.create_with_mnemonic()  # Cambiado para extraer correctamente address y mnemonic

        # Detalles de la cartera
        wallet_details = {
            "address": account.address,
            "private_key": account.key.hex(),  # Cambio realizado aquí
            "mnemonic": mnemonic  # Tomamos el valor directamente
        }

        # Guardar los detalles en un archivo .txt
        self.save_wallet_details(wallet_details)

    def save_wallet_details(self, details):
        filename = f"wallet_{details['address']}.txt"
        with open(filename, 'w') as file:
            file.write(f"Address: {details['address']}\n")
            file.write(f"Private Key: {details['private_key']}\n")
            file.write(f"Mnemonic: {details['mnemonic']}\n")
            file.write("Compatible Networks: Arbitrum, Aurora, Avalanche, C-Chain, Base, Blast, Boba, BounceBit, Callisto, Celo, Conflux, eSpace, Ethereum, Classic, Cronos, Chain, Ethereum, Evmos, Fantom, GoChain, ECO, Chain, IoTeX, EVM, K, Kaia, KavaEvm, KuCoin, Community, Chain, Linea, Manta, Pacific, Mantle, Merlin, Metis, Moonbeam, Moonriver, Neon, OpBNB, Optimism, Polygon, Polygon, zkEVM, Scroll, Smart, Chain, ThunderCore, V, Viction, Wanchain, xDai, Zeta, EVM, Z, ZkLinkNova, Zksync.\n")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WalletApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()