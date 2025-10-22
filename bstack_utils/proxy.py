# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll1l11l_opy_
bstack111ll1ll_opy_ = Config.bstack1llll1lll_opy_()
def bstack11l1ll1l111_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1ll11ll1_opy_(bstack11l1ll11l1l_opy_, bstack11l1ll11lll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll11l1l_opy_):
        with open(bstack11l1ll11l1l_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1ll1l111_opy_(bstack11l1ll11l1l_opy_):
        pac = get_pac(url=bstack11l1ll11l1l_opy_)
    else:
        raise Exception(bstack11l1l11_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭ᝮ").format(bstack11l1ll11l1l_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l1l11_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣᝯ"), 80))
        bstack11l1ll11l11_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll11l11_opy_ = bstack11l1l11_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩᝰ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll11lll_opy_, bstack11l1ll11l11_opy_)
    return proxy_url
def bstack111ll11l11_opy_(config):
    return bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᝱") in config or bstack11l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᝲ") in config
def bstack1l1lllll1l_opy_(config):
    if not bstack111ll11l11_opy_(config):
        return
    if config.get(bstack11l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᝳ")):
        return config.get(bstack11l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᝴"))
    if config.get(bstack11l1l11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ᝵")):
        return config.get(bstack11l1l11_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᝶"))
def bstack11l11l1111_opy_(config, bstack11l1ll11lll_opy_):
    proxy = bstack1l1lllll1l_opy_(config)
    proxies = {}
    if config.get(bstack11l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ᝷")) or config.get(bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭᝸")):
        if proxy.endswith(bstack11l1l11_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ᝹")):
            proxies = bstack1l1ll1lll1_opy_(proxy, bstack11l1ll11lll_opy_)
        else:
            proxies = {
                bstack11l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪ᝺"): proxy
            }
    bstack111ll1ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬ᝻"), proxies)
    return proxies
def bstack1l1ll1lll1_opy_(bstack11l1ll11l1l_opy_, bstack11l1ll11lll_opy_):
    proxies = {}
    global bstack11l1ll1l1ll_opy_
    if bstack11l1l11_opy_ (u"࠭ࡐࡂࡅࡢࡔࡗࡕࡘ࡚ࠩ᝼") in globals():
        return bstack11l1ll1l1ll_opy_
    try:
        proxy = bstack11l1ll11ll1_opy_(bstack11l1ll11l1l_opy_, bstack11l1ll11lll_opy_)
        if bstack11l1l11_opy_ (u"ࠢࡅࡋࡕࡉࡈ࡚ࠢ᝽") in proxy:
            proxies = {}
        elif bstack11l1l11_opy_ (u"ࠣࡊࡗࡘࡕࠨ᝾") in proxy or bstack11l1l11_opy_ (u"ࠤࡋࡘ࡙ࡖࡓࠣ᝿") in proxy or bstack11l1l11_opy_ (u"ࠥࡗࡔࡉࡋࡔࠤក") in proxy:
            bstack11l1ll1l1l1_opy_ = proxy.split(bstack11l1l11_opy_ (u"ࠦࠥࠨខ"))
            if bstack11l1l11_opy_ (u"ࠧࡀ࠯࠰ࠤគ") in bstack11l1l11_opy_ (u"ࠨࠢឃ").join(bstack11l1ll1l1l1_opy_[1:]):
                proxies = {
                    bstack11l1l11_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ង"): bstack11l1l11_opy_ (u"ࠣࠤច").join(bstack11l1ll1l1l1_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨឆ"): str(bstack11l1ll1l1l1_opy_[0]).lower() + bstack11l1l11_opy_ (u"ࠥ࠾࠴࠵ࠢជ") + bstack11l1l11_opy_ (u"ࠦࠧឈ").join(bstack11l1ll1l1l1_opy_[1:])
                }
        elif bstack11l1l11_opy_ (u"ࠧࡖࡒࡐ࡚࡜ࠦញ") in proxy:
            bstack11l1ll1l1l1_opy_ = proxy.split(bstack11l1l11_opy_ (u"ࠨࠠࠣដ"))
            if bstack11l1l11_opy_ (u"ࠢ࠻࠱࠲ࠦឋ") in bstack11l1l11_opy_ (u"ࠣࠤឌ").join(bstack11l1ll1l1l1_opy_[1:]):
                proxies = {
                    bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨឍ"): bstack11l1l11_opy_ (u"ࠥࠦណ").join(bstack11l1ll1l1l1_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪត"): bstack11l1l11_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨថ") + bstack11l1l11_opy_ (u"ࠨࠢទ").join(bstack11l1ll1l1l1_opy_[1:])
                }
        else:
            proxies = {
                bstack11l1l11_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ធ"): proxy
            }
    except Exception as e:
        print(bstack11l1l11_opy_ (u"ࠣࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧន"), bstack11l1ll1l11l_opy_.format(bstack11l1ll11l1l_opy_, str(e)))
    bstack11l1ll1l1ll_opy_ = proxies
    return proxies