# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1lll1l11_opy_
bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
def bstack11l1lll1l1l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1lll1111_opy_(bstack11l1lll11l1_opy_, bstack11l1lll1ll1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1lll11l1_opy_):
        with open(bstack11l1lll11l1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1lll1l1l_opy_(bstack11l1lll11l1_opy_):
        pac = get_pac(url=bstack11l1lll11l1_opy_)
    else:
        raise Exception(bstack11l1l11_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬᝊ").format(bstack11l1lll11l1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l1l11_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢᝋ"), 80))
        bstack11l1lll11ll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1lll11ll_opy_ = bstack11l1l11_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨᝌ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1lll1ll1_opy_, bstack11l1lll11ll_opy_)
    return proxy_url
def bstack11l11lll1l_opy_(config):
    return bstack11l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᝍ") in config or bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᝎ") in config
def bstack1l111ll1l_opy_(config):
    if not bstack11l11lll1l_opy_(config):
        return
    if config.get(bstack11l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᝏ")):
        return config.get(bstack11l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᝐ"))
    if config.get(bstack11l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᝑ")):
        return config.get(bstack11l1l11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᝒ"))
def bstack1l1l1l1111_opy_(config, bstack11l1lll1ll1_opy_):
    proxy = bstack1l111ll1l_opy_(config)
    proxies = {}
    if config.get(bstack11l1l11_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᝓ")) or config.get(bstack11l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᝔")):
        if proxy.endswith(bstack11l1l11_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ᝕")):
            proxies = bstack1l1ll111ll_opy_(proxy, bstack11l1lll1ll1_opy_)
        else:
            proxies = {
                bstack11l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩ᝖"): proxy
            }
    bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠫ᝗"), proxies)
    return proxies
def bstack1l1ll111ll_opy_(bstack11l1lll11l1_opy_, bstack11l1lll1ll1_opy_):
    proxies = {}
    global bstack11l1lll111l_opy_
    if bstack11l1l11_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨ᝘") in globals():
        return bstack11l1lll111l_opy_
    try:
        proxy = bstack11l1lll1111_opy_(bstack11l1lll11l1_opy_, bstack11l1lll1ll1_opy_)
        if bstack11l1l11_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨ᝙") in proxy:
            proxies = {}
        elif bstack11l1l11_opy_ (u"ࠢࡉࡖࡗࡔࠧ᝚") in proxy or bstack11l1l11_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢ᝛") in proxy or bstack11l1l11_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣ᝜") in proxy:
            bstack11l1ll1llll_opy_ = proxy.split(bstack11l1l11_opy_ (u"ࠥࠤࠧ᝝"))
            if bstack11l1l11_opy_ (u"ࠦ࠿࠵࠯ࠣ᝞") in bstack11l1l11_opy_ (u"ࠧࠨ᝟").join(bstack11l1ll1llll_opy_[1:]):
                proxies = {
                    bstack11l1l11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᝠ"): bstack11l1l11_opy_ (u"ࠢࠣᝡ").join(bstack11l1ll1llll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᝢ"): str(bstack11l1ll1llll_opy_[0]).lower() + bstack11l1l11_opy_ (u"ࠤ࠽࠳࠴ࠨᝣ") + bstack11l1l11_opy_ (u"ࠥࠦᝤ").join(bstack11l1ll1llll_opy_[1:])
                }
        elif bstack11l1l11_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥᝥ") in proxy:
            bstack11l1ll1llll_opy_ = proxy.split(bstack11l1l11_opy_ (u"ࠧࠦࠢᝦ"))
            if bstack11l1l11_opy_ (u"ࠨ࠺࠰࠱ࠥᝧ") in bstack11l1l11_opy_ (u"ࠢࠣᝨ").join(bstack11l1ll1llll_opy_[1:]):
                proxies = {
                    bstack11l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᝩ"): bstack11l1l11_opy_ (u"ࠤࠥᝪ").join(bstack11l1ll1llll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᝫ"): bstack11l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᝬ") + bstack11l1l11_opy_ (u"ࠧࠨ᝭").join(bstack11l1ll1llll_opy_[1:])
                }
        else:
            proxies = {
                bstack11l1l11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᝮ"): proxy
            }
    except Exception as e:
        print(bstack11l1l11_opy_ (u"ࠢࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦᝯ"), bstack11l1lll1l11_opy_.format(bstack11l1lll11l1_opy_, str(e)))
    bstack11l1lll111l_opy_ = proxies
    return proxies