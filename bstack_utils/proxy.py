# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll1l1ll_opy_
bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
def bstack11l1ll1l11l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1ll1l111_opy_(bstack11l1ll11ll1_opy_, bstack11l1ll1l1l1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll11ll1_opy_):
        with open(bstack11l1ll11ll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1ll1l11l_opy_(bstack11l1ll11ll1_opy_):
        pac = get_pac(url=bstack11l1ll11ll1_opy_)
    else:
        raise Exception(bstack1lllll1l_opy_ (u"ࠪࡔࡦࡩࠠࡧ࡫࡯ࡩࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡀࠠࡼࡿࠪᝲ").format(bstack11l1ll11ll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1lllll1l_opy_ (u"ࠦ࠽࠴࠸࠯࠺࠱࠼ࠧᝳ"), 80))
        bstack11l1ll11lll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll11lll_opy_ = bstack1lllll1l_opy_ (u"ࠬ࠶࠮࠱࠰࠳࠲࠵࠭᝴")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll1l1l1_opy_, bstack11l1ll11lll_opy_)
    return proxy_url
def bstack1l1l1l11ll_opy_(config):
    return bstack1lllll1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ᝵") in config or bstack1lllll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᝶") in config
def bstack111l11ll1_opy_(config):
    if not bstack1l1l1l11ll_opy_(config):
        return
    if config.get(bstack1lllll1l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ᝷")):
        return config.get(bstack1lllll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᝸"))
    if config.get(bstack1lllll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᝹")):
        return config.get(bstack1lllll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᝺"))
def bstack1ll111lll_opy_(config, bstack11l1ll1l1l1_opy_):
    proxy = bstack111l11ll1_opy_(config)
    proxies = {}
    if config.get(bstack1lllll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᝻")) or config.get(bstack1lllll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ᝼")):
        if proxy.endswith(bstack1lllll1l_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ᝽")):
            proxies = bstack11l1111lll_opy_(proxy, bstack11l1ll1l1l1_opy_)
        else:
            proxies = {
                bstack1lllll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧ᝾"): proxy
            }
    bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠩ᝿"), proxies)
    return proxies
def bstack11l1111lll_opy_(bstack11l1ll11ll1_opy_, bstack11l1ll1l1l1_opy_):
    proxies = {}
    global bstack11l1ll1ll11_opy_
    if bstack1lllll1l_opy_ (u"ࠪࡔࡆࡉ࡟ࡑࡔࡒ࡜࡞࠭ក") in globals():
        return bstack11l1ll1ll11_opy_
    try:
        proxy = bstack11l1ll1l111_opy_(bstack11l1ll11ll1_opy_, bstack11l1ll1l1l1_opy_)
        if bstack1lllll1l_opy_ (u"ࠦࡉࡏࡒࡆࡅࡗࠦខ") in proxy:
            proxies = {}
        elif bstack1lllll1l_opy_ (u"ࠧࡎࡔࡕࡒࠥគ") in proxy or bstack1lllll1l_opy_ (u"ࠨࡈࡕࡖࡓࡗࠧឃ") in proxy or bstack1lllll1l_opy_ (u"ࠢࡔࡑࡆࡏࡘࠨង") in proxy:
            bstack11l1ll1ll1l_opy_ = proxy.split(bstack1lllll1l_opy_ (u"ࠣࠢࠥច"))
            if bstack1lllll1l_opy_ (u"ࠤ࠽࠳࠴ࠨឆ") in bstack1lllll1l_opy_ (u"ࠥࠦជ").join(bstack11l1ll1ll1l_opy_[1:]):
                proxies = {
                    bstack1lllll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪឈ"): bstack1lllll1l_opy_ (u"ࠧࠨញ").join(bstack11l1ll1ll1l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1lllll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬដ"): str(bstack11l1ll1ll1l_opy_[0]).lower() + bstack1lllll1l_opy_ (u"ࠢ࠻࠱࠲ࠦឋ") + bstack1lllll1l_opy_ (u"ࠣࠤឌ").join(bstack11l1ll1ll1l_opy_[1:])
                }
        elif bstack1lllll1l_opy_ (u"ࠤࡓࡖࡔ࡞࡙ࠣឍ") in proxy:
            bstack11l1ll1ll1l_opy_ = proxy.split(bstack1lllll1l_opy_ (u"ࠥࠤࠧណ"))
            if bstack1lllll1l_opy_ (u"ࠦ࠿࠵࠯ࠣត") in bstack1lllll1l_opy_ (u"ࠧࠨថ").join(bstack11l1ll1ll1l_opy_[1:]):
                proxies = {
                    bstack1lllll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬទ"): bstack1lllll1l_opy_ (u"ࠢࠣធ").join(bstack11l1ll1ll1l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1lllll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧន"): bstack1lllll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥប") + bstack1lllll1l_opy_ (u"ࠥࠦផ").join(bstack11l1ll1ll1l_opy_[1:])
                }
        else:
            proxies = {
                bstack1lllll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪព"): proxy
            }
    except Exception as e:
        print(bstack1lllll1l_opy_ (u"ࠧࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤភ"), bstack11l1ll1l1ll_opy_.format(bstack11l1ll11ll1_opy_, str(e)))
    bstack11l1ll1ll11_opy_ = proxies
    return proxies