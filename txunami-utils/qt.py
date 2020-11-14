import json
from PyQt5.QtWidgets import qApp

from electroncash.i18n import _
from electroncash.plugins import BasePlugin, hook

class Plugin(BasePlugin):
    electrumcash_qt_gui = None
    is_version_compatible = True

    def __init__(self, parent, config, name):
        BasePlugin.__init__(self, parent, config, name)

    def fullname(self):
        return 'Txunami Utilities'

    def diagnostic_name(self):
        return "TxunamiUtilities"

    def description(self):
        return _("Provides some helpers for txunami configuration")

    def make_inputs(self, utxo_list, selected):
        # Example txunami input format:
        # {
        #     "txid": "6a1393e4b4ef3c8067a82b90e8bd6e5d331249459e46b543736befdcb86acaad",
        #     "vout": 0,
        #     "address": "bchtest:qqcmuc3dgf6k38f0a8nfgaxr44udawzq2vgvuxyyyj",
        #     "scriptPubKey": "76a91431be622d4275689d2fe9e69474c3ad78deb8405388ac",
        #     "satoshi": 10000000000,
        #     "privKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        # },

        wallet = utxo_list.wallet
        txunami_ins = []

        for name, flags in selected.items():
            txid, tn = name.split(':')
            n = int(tn)
            tx = wallet.transactions[txid]
            txo = tx.get_outputs()[n]
            txunami_ins.append({
                'txid': txid,
                'vout': n,
                'address': txo[0].to_full_ui_string(),
                'scriptPubKey': txo[0].to_script_hex(),
                'satoshi': txo[1],
                'privKey': wallet.export_private_key(txo[0], None)
            })

        return txunami_ins


    def copy_inputs(self, utxo_list, selected):
        txunami_ins = self.make_inputs(utxo_list, selected)
        jsout = json.dumps(txunami_ins, indent=4)
        qApp.clipboard().setText(jsout)

    @hook
    def utxo_list_context_menu_setup(self, utxo_list, menu, selected):
        menu.addAction(_("Copy as Txunami Inputs"), lambda: self.copy_inputs(utxo_list, selected))
