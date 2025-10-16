# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1llll111_opy_
bstack11l1111l_opy_ = Config.bstack11111l1l_opy_()
def bstack11l1lll11ll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1lll1lll_opy_(bstack11l1lll1l11_opy_, bstack11l1lll111l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1lll1l11_opy_):
        with open(bstack11l1lll1l11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1lll11ll_opy_(bstack11l1lll1l11_opy_):
        pac = get_pac(url=bstack11l1lll1l11_opy_)
    else:
        raise Exception(bstack1lllll1_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭ᝒ").format(bstack11l1lll1l11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1lllll1_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣᝓ"), 80))
        bstack11l1lll11l1_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1lll11l1_opy_ = bstack1lllll1_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩ᝔")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1lll111l_opy_, bstack11l1lll11l1_opy_)
    return proxy_url
def bstack11lll1lll_opy_(config):
    return bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᝕") in config or bstack1lllll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᝖") in config
def bstack1ll1ll1lll_opy_(config):
    if not bstack11lll1lll_opy_(config):
        return
    if config.get(bstack1lllll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ᝗")):
        return config.get(bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᝘"))
    if config.get(bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ᝙")):
        return config.get(bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᝚"))
def bstack111l111l1_opy_(config, bstack11l1lll111l_opy_):
    proxy = bstack1ll1ll1lll_opy_(config)
    proxies = {}
    if config.get(bstack1lllll1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ᝛")) or config.get(bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭᝜")):
        if proxy.endswith(bstack1lllll1_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ᝝")):
            proxies = bstack1l1l1l111l_opy_(proxy, bstack11l1lll111l_opy_)
        else:
            proxies = {
                bstack1lllll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪ᝞"): proxy
            }
    bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬ᝟"), proxies)
    return proxies
def bstack1l1l1l111l_opy_(bstack11l1lll1l11_opy_, bstack11l1lll111l_opy_):
    proxies = {}
    global bstack11l1lll1ll1_opy_
    if bstack1lllll1_opy_ (u"࠭ࡐࡂࡅࡢࡔࡗࡕࡘ࡚ࠩᝠ") in globals():
        return bstack11l1lll1ll1_opy_
    try:
        proxy = bstack11l1lll1lll_opy_(bstack11l1lll1l11_opy_, bstack11l1lll111l_opy_)
        if bstack1lllll1_opy_ (u"ࠢࡅࡋࡕࡉࡈ࡚ࠢᝡ") in proxy:
            proxies = {}
        elif bstack1lllll1_opy_ (u"ࠣࡊࡗࡘࡕࠨᝢ") in proxy or bstack1lllll1_opy_ (u"ࠤࡋࡘ࡙ࡖࡓࠣᝣ") in proxy or bstack1lllll1_opy_ (u"ࠥࡗࡔࡉࡋࡔࠤᝤ") in proxy:
            bstack11l1lll1l1l_opy_ = proxy.split(bstack1lllll1_opy_ (u"ࠦࠥࠨᝥ"))
            if bstack1lllll1_opy_ (u"ࠧࡀ࠯࠰ࠤᝦ") in bstack1lllll1_opy_ (u"ࠨࠢᝧ").join(bstack11l1lll1l1l_opy_[1:]):
                proxies = {
                    bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᝨ"): bstack1lllll1_opy_ (u"ࠣࠤᝩ").join(bstack11l1lll1l1l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᝪ"): str(bstack11l1lll1l1l_opy_[0]).lower() + bstack1lllll1_opy_ (u"ࠥ࠾࠴࠵ࠢᝫ") + bstack1lllll1_opy_ (u"ࠦࠧᝬ").join(bstack11l1lll1l1l_opy_[1:])
                }
        elif bstack1lllll1_opy_ (u"ࠧࡖࡒࡐ࡚࡜ࠦ᝭") in proxy:
            bstack11l1lll1l1l_opy_ = proxy.split(bstack1lllll1_opy_ (u"ࠨࠠࠣᝮ"))
            if bstack1lllll1_opy_ (u"ࠢ࠻࠱࠲ࠦᝯ") in bstack1lllll1_opy_ (u"ࠣࠤᝰ").join(bstack11l1lll1l1l_opy_[1:]):
                proxies = {
                    bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨ᝱"): bstack1lllll1_opy_ (u"ࠥࠦᝲ").join(bstack11l1lll1l1l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1lllll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᝳ"): bstack1lllll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ᝴") + bstack1lllll1_opy_ (u"ࠨࠢ᝵").join(bstack11l1lll1l1l_opy_[1:])
                }
        else:
            proxies = {
                bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭᝶"): proxy
            }
    except Exception as e:
        print(bstack1lllll1_opy_ (u"ࠣࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧ᝷"), bstack11l1llll111_opy_.format(bstack11l1lll1l11_opy_, str(e)))
    bstack11l1lll1ll1_opy_ = proxies
    return proxies