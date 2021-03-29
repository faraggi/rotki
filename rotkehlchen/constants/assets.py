from rotkehlchen.assets.asset import Asset, EthereumToken

A_USD = Asset('USD')
A_BTC = Asset('BTC')
A_BCH = Asset('BCH')

A_BSV = Asset('BSV')
A_ETH = Asset('ETH')
A_ETH2 = Asset('ETH2')
A_ETC = Asset('ETC')
A_KSM = Asset('KSM')

A_BAL = EthereumToken('0xba100000625a3754423978a60c9317c58a424e3D')
A_BAT = EthereumToken('0x0D8775F648430679A709E98d2b0Cb6250d2887EF')
A_UNI = EthereumToken('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984')
A_1INCH = EthereumToken('0x111111111117dC0aa78b770fA6A738034120C302')
A_DAI = EthereumToken('0x6B175474E89094C44Da98b954EedeAC495271d0F')
A_SAI = EthereumToken('0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359')
A_YFI = EthereumToken('0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e')
A_USDT = EthereumToken('0xdAC17F958D2ee523a2206206994597C13D831ec7')
A_USDC = EthereumToken('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
A_TUSD = EthereumToken('0x0000000000085d4780B73119b644AE5ecd22b376')

A_AAVE = EthereumToken('0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9')
A_GUSD = EthereumToken('0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd')
A_CRV = EthereumToken('0xD533a949740bb3306d119CC777fa900bA034cd52')
A_KNC = EthereumToken('0xdd974D5C2e2928deA5F71b9825b8b646686BD200')
A_WBTC = EthereumToken('0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599')
A_WETH = EthereumToken('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')
A_ZRX = EthereumToken('0xE41d2489571d322189246DaFA5ebDe1F4699F498')
A_MANA = EthereumToken('0x0F5D2fB29fb7d3CFeE444a200298f468908cC942')
A_PAX = EthereumToken('0x8E870D67F660D95d5be530380D0eC0bd388289E1')
A_COMP = EthereumToken('0xc00e94Cb662C3520282E6f5717214004A7f26888')
A_LRC = EthereumToken('0xBBbbCA6A901c926F240b89EacB641d8Aec7AEafD')
A_LINK = EthereumToken('0x514910771AF9Ca656af840dff83E8264EcF986CA')
A_ADX = EthereumToken('0xADE00C28244d5CE17D72E40330B1c318cD12B7c3')
A_TORN = EthereumToken('0x77777FeDdddFfC19Ff86DB637967013e6C6A116C')
A_CORN = EthereumToken('0xa456b515303B2Ce344E9d2601f91270f8c2Fea5E')
A_GRAIN = EthereumToken('0x6589fe1271A0F29346796C6bAf0cdF619e25e58e')
A_COMBO = EthereumToken('0xfFffFffF2ba8F66D4e51811C5190992176930278')
A_LDO = EthereumToken('0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32')
A_RENBTC = EthereumToken('0xEB4C2781e4ebA804CE9a9803C67d0893436bB27D')
A_BNB = EthereumToken('0xB8c77482e45F1F44dE1745F52C74426C631bDD52')
A_REP = EthereumToken('0x221657776846890989a759BA2973e427DfF5C9bB')  # v2
A_BZRX = EthereumToken('0x56d811088235F11C8920698a204A5010a788f4b3')
A_CDAI = EthereumToken('0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643')
A_CUSDC = EthereumToken('0x39AA39c021dfbaE8faC545936693aC917d5E7563')
A_STAKE = EthereumToken('0x0Ae055097C6d159879521C384F1D2123D1f195e6')
A_DPI = EthereumToken('0x1494CA1F11D487c2bBe4543E90080AeBa4BA3C2b')
A_YFII = EthereumToken('0xa1d0E215a23d7030842FC67cE582a6aFa3CCaB83')
A_MCB = EthereumToken('0x4e352cF164E64ADCBad318C3a1e222E9EBa4Ce42')

# used as underlying assets of aave v1 tokens
A_ENJ = EthereumToken('0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c')
A_SUSD = EthereumToken('0x57Ab1ec28D129707052df4dF418D58a2D46d5f51')
A_BUSD = EthereumToken('0x4Fabb145d64652a948d72533023f6E7A623C7C53')
A_LEND = EthereumToken('0x80fB784B7eD66730e8b1DBd9820aFD29931aab03')
A_MKR = EthereumToken('0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2')
A_REN = EthereumToken('0x408e41876cCCDC0F92210600ef50372656052a38')
A_SNX = EthereumToken('0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F')

# atokens TODO: These can be handled programatically if enough info is in the assets DB
# protocol and underlying asset

A_ALINK_V1 = EthereumToken('0xA64BD6C70Cb9051F6A9ba1F163Fdc07E0DfB5F84')
A_AETH_V1 = EthereumToken('0x3a3A65aAb0dd2A17E3F1947bA16138cd37d08c04')
A_AENJ_V1 = EthereumToken('0x712DB54daA836B53Ef1EcBb9c6ba3b9Efb073F40')
A_ADAI_V1 = EthereumToken('0xfC1E690f61EFd961294b3e1Ce3313fBD8aa4f85d')
A_AUSDC_V1 = EthereumToken('0x9bA00D6856a4eDF4665BcA2C2309936572473B7E')
A_ASUSD_V1 = EthereumToken('0x625aE63000f46200499120B906716420bd059240')
A_ATUSD_V1 = EthereumToken('0x4DA9b813057D04BAef4e5800E36083717b4a0341')
A_AUSDT_V1 = EthereumToken('0x71fc860F7D3A592A4a98740e39dB31d25db65ae8')
A_ABUSD_V1 = EthereumToken('0x6Ee0f7BB50a54AB5253dA0667B0Dc2ee526C30a8')
A_ABAT_V1 = EthereumToken('0xE1BA0FB44CCb0D11b80F92f4f8Ed94CA3fF51D00')
A_AKNC_V1 = EthereumToken('0x9D91BE44C06d373a8a226E1f3b146956083803eB')
A_ALEND_V1 = EthereumToken('0x7D2D3688Df45Ce7C552E19c27e007673da9204B8')
A_AMANA_V1 = EthereumToken('0x6FCE4A401B6B80ACe52baAefE4421Bd188e76F6f')
A_AMKR_V1 = EthereumToken('0x7deB5e830be29F91E298ba5FF1356BB7f8146998')
A_AREP_V1 = EthereumToken('0x71010A9D003445aC60C4e6A7017c1E89A477B438')
A_AREN_V1 = EthereumToken('0x69948cC03f478B95283F7dbf1CE764d0fc7EC54C')
A_ASNX_V1 = EthereumToken('0x328C4c80BC7aCa0834Db37e6600A6c49E12Da4DE')
A_AWBTC_V1 = EthereumToken('0xFC4B8ED459e00e5400be803A9BB3954234FD50e3')
A_AYFI_V1 = EthereumToken('0x12e51E77DAAA58aA0E9247db7510Ea4B46F9bEAd')
A_AZRX_V1 = EthereumToken('0x6Fb0855c404E09c47C3fBCA25f08d4E41f9F062f')
A_AAAVE_V1 = EthereumToken('0xba3D9687Cf50fE253cd2e1cFeEdE1d6787344Ed5')
A_AUNI_V1 = EthereumToken('0xB124541127A0A657f056D9Dd06188c4F1b0e5aab')


# Special tokens for defi price inquiry -- these should end up in programmatic rules
# after being upgraded to include, protocol (to identify the program to run on them)
# and underlying assets
A_YV1_DAIUSDCTBUSD = EthereumToken('0x2994529C0652D127b7842094103715ec5299bBed')
A_CRVP_DAIUSDCTBUSD = EthereumToken('0x3B3Ac5386837Dc563660FB6a0937DFAa5924333B')
A_YV1_DAIUSDCTTUSD = EthereumToken('0x5dbcF33D8c2E976c6b560249878e6F1491Bca25c')
A_CRVP_DAIUSDCTTUSD = EthereumToken('0xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8')
A_CRVP_RENWSBTC = EthereumToken('0x075b1bb99792c9E1041bA13afEf80C91a1e70fB3')
A_YV1_RENWSBTC = EthereumToken('0x7Ff566E1d69DEfF32a7b244aE7276b9f90e9D0f6')
A_CRV_RENWBTC = EthereumToken('0x49849C98ae39Fff122806C06791Fa73784FB3675')
A_CRV_YPAX = EthereumToken('0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8')
A_CRV_GUSD = EthereumToken('0xD2967f45c4f384DEEa880F807Be904762a3DeA07')
A_CRV_3CRV = EthereumToken('0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490')
A_YV1_3CRV = EthereumToken('0x9cA85572E6A3EbF24dEDd195623F188735A5179f')
A_CRV_3CRVSUSD = EthereumToken('0xC25a3A3b969415c80451098fa907EC722572917F')
A_YV1_ALINK = EthereumToken('0x29E240CFD7946BA20895a7a02eDb25C210f9f324')
A_YV1_DAI = EthereumToken('0xACd43E627e64355f1861cEC6d3a6688B31a6F952')
A_YV1_WETH = EthereumToken('0xe1237aA7f535b0CC33Fd973D66cBf830354D16c7')
A_YV1_YFI = EthereumToken('0xBA2E7Fed597fd0E3e70f5130BcDbbFE06bB94fe1')
A_YV1_USDT = EthereumToken('0x2f08119C6f07c006695E079AAFc638b8789FAf18')
A_YV1_USDC = EthereumToken('0x597aD1e0c13Bfe8025993D9e79C69E1c0233522e')
A_YV1_TUSD = EthereumToken('0x37d19d1c4E1fa9DC47bD1eA12f742a0887eDa74a')
A_YV1_GUSD = EthereumToken('0xec0d8D3ED5477106c6D4ea27D90a60e594693C90')
A_FARM_USDC = EthereumToken('0xf0358e8c3CD5Fa238a29301d0bEa3D63A17bEdBE')
A_FARM_USDT = EthereumToken('0x053c80eA73Dc6941F518a68E2FC52Ac45BDE7c9C')
A_FARM_DAI = EthereumToken('0xab7FA2B2985BCcfC13c6D86b1D5A17486ab1e04C')
A_FARM_TUSD = EthereumToken('0x7674622c63Bee7F46E86a4A5A18976693D54441b')
A_FARM_WETH = EthereumToken('0xFE09e53A81Fe2808bc493ea64319109B5bAa573e')
A_FARM_WBTC = EthereumToken('0x5d9d25c7C457dD82fc8668FFC6B9746b674d4EcB')
A_FARM_RENBTC = EthereumToken('0xC391d1b08c1403313B0c28D47202DFDA015633C4')
A_FARM_CRVRENWBTC = EthereumToken('0x9aA8F427A17d6B0d91B6262989EdC7D45d6aEdf8')
