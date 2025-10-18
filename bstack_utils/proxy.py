# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll1ll11_opy_
bstack11111l11_opy_ = Config.bstack111l11l1_opy_()
def bstack11l1ll11lll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1ll1l1l1_opy_(bstack11l1ll1l111_opy_, bstack11l1ll1l11l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll1l111_opy_):
        with open(bstack11l1ll1l111_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1ll11lll_opy_(bstack11l1ll1l111_opy_):
        pac = get_pac(url=bstack11l1ll1l111_opy_)
    else:
        raise Exception(bstack11l111_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬ᝴").format(bstack11l1ll1l111_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l111_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢ᝵"), 80))
        bstack11l1ll11ll1_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll11ll1_opy_ = bstack11l111_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨ᝶")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll1l11l_opy_, bstack11l1ll11ll1_opy_)
    return proxy_url
def bstack1lll1l1l1l_opy_(config):
    return bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ᝷") in config or bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭᝸") in config
def bstack11l1llllll_opy_(config):
    if not bstack1lll1l1l1l_opy_(config):
        return
    if config.get(bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᝹")):
        return config.get(bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ᝺"))
    if config.get(bstack11l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ᝻")):
        return config.get(bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ᝼"))
def bstack11l11l1l11_opy_(config, bstack11l1ll1l11l_opy_):
    proxy = bstack11l1llllll_opy_(config)
    proxies = {}
    if config.get(bstack11l111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ᝽")) or config.get(bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᝾")):
        if proxy.endswith(bstack11l111_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ᝿")):
            proxies = bstack11ll11lll_opy_(proxy, bstack11l1ll1l11l_opy_)
        else:
            proxies = {
                bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩក"): proxy
            }
    bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠫខ"), proxies)
    return proxies
def bstack11ll11lll_opy_(bstack11l1ll1l111_opy_, bstack11l1ll1l11l_opy_):
    proxies = {}
    global bstack11l1ll1l1ll_opy_
    if bstack11l111_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨគ") in globals():
        return bstack11l1ll1l1ll_opy_
    try:
        proxy = bstack11l1ll1l1l1_opy_(bstack11l1ll1l111_opy_, bstack11l1ll1l11l_opy_)
        if bstack11l111_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨឃ") in proxy:
            proxies = {}
        elif bstack11l111_opy_ (u"ࠢࡉࡖࡗࡔࠧង") in proxy or bstack11l111_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢច") in proxy or bstack11l111_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣឆ") in proxy:
            bstack11l1ll1ll1l_opy_ = proxy.split(bstack11l111_opy_ (u"ࠥࠤࠧជ"))
            if bstack11l111_opy_ (u"ࠦ࠿࠵࠯ࠣឈ") in bstack11l111_opy_ (u"ࠧࠨញ").join(bstack11l1ll1ll1l_opy_[1:]):
                proxies = {
                    bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬដ"): bstack11l111_opy_ (u"ࠢࠣឋ").join(bstack11l1ll1ll1l_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧឌ"): str(bstack11l1ll1ll1l_opy_[0]).lower() + bstack11l111_opy_ (u"ࠤ࠽࠳࠴ࠨឍ") + bstack11l111_opy_ (u"ࠥࠦណ").join(bstack11l1ll1ll1l_opy_[1:])
                }
        elif bstack11l111_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥត") in proxy:
            bstack11l1ll1ll1l_opy_ = proxy.split(bstack11l111_opy_ (u"ࠧࠦࠢថ"))
            if bstack11l111_opy_ (u"ࠨ࠺࠰࠱ࠥទ") in bstack11l111_opy_ (u"ࠢࠣធ").join(bstack11l1ll1ll1l_opy_[1:]):
                proxies = {
                    bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧន"): bstack11l111_opy_ (u"ࠤࠥប").join(bstack11l1ll1ll1l_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩផ"): bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧព") + bstack11l111_opy_ (u"ࠧࠨភ").join(bstack11l1ll1ll1l_opy_[1:])
                }
        else:
            proxies = {
                bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬម"): proxy
            }
    except Exception as e:
        print(bstack11l111_opy_ (u"ࠢࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦយ"), bstack11l1ll1ll11_opy_.format(bstack11l1ll1l111_opy_, str(e)))
    bstack11l1ll1l1ll_opy_ = proxies
    return proxies