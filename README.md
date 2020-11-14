# Txunami Utilities plugin

This allows you to easily select UTXOs in Electron Cash and use them as inputs to [txunami](https://github.com/gandrewstone/txunami).

## Installation 

Download the latest [release](https://github.com/EchterAgo/txunami-utils-ec-plugin/releases) (which will be a .zip file), [verify](https://github.com/Electron-Cash/keys-n-hashes#2-verify-sha256-digest-hash) it against [my public key](https://raw.githubusercontent.com/Electron-Cash/Electron-Cash/master/pubkeys/axelkey.txt), open Electron Cash, click the “Tools” drop down menu, click “Installed Plugins”, click "Add Plugin", find and open the zip file and follow the dialog to complete the installation.

## Usage

Go to the coins tab, select the coins you want to use, right click them and select "Copy as Txunami Inputs". Your clipboard will now contain the inputs and you can paste them into your `txunami.json` configuration file into the `coins` section.

## Limitations

* Wallet passwords or hardware wallets are not supported. Only wallets that can export their private keys can be used.

## Donations

* Cash Account: ichundes#102
* bitcoincash:qpup92thur2ev8g6x306a4apcx2tfjd8duupg8w9k7
