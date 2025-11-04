# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1l1llll1_opy_
bstack1llll11ll_opy_ = Config.bstack1llllllll_opy_()
def bstack11l1ll11111_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1ll111l1_opy_(bstack11l1l1lll1l_opy_, bstack11l1ll1111l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1l1lll1l_opy_):
        with open(bstack11l1l1lll1l_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1ll11111_opy_(bstack11l1l1lll1l_opy_):
        pac = get_pac(url=bstack11l1l1lll1l_opy_)
    else:
        raise Exception(bstack11l1111_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬថ").format(bstack11l1l1lll1l_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l1111_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢទ"), 80))
        bstack11l1l1lllll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1l1lllll_opy_ = bstack11l1111_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨធ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll1111l_opy_, bstack11l1l1lllll_opy_)
    return proxy_url
def bstack111l1l1l11_opy_(config):
    return bstack11l1111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫន") in config or bstack11l1111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ប") in config
def bstack111lll1ll_opy_(config):
    if not bstack111l1l1l11_opy_(config):
        return
    if config.get(bstack11l1111_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ផ")):
        return config.get(bstack11l1111_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧព"))
    if config.get(bstack11l1111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩភ")):
        return config.get(bstack11l1111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪម"))
def bstack1111l1l111_opy_(config, bstack11l1ll1111l_opy_):
    proxy = bstack111lll1ll_opy_(config)
    proxies = {}
    if config.get(bstack11l1111_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪយ")) or config.get(bstack11l1111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬរ")):
        if proxy.endswith(bstack11l1111_opy_ (u"ࠩ࠱ࡴࡦࡩࠧល")):
            proxies = bstack1l1ll11ll_opy_(proxy, bstack11l1ll1111l_opy_)
        else:
            proxies = {
                bstack11l1111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩវ"): proxy
            }
    bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠫឝ"), proxies)
    return proxies
def bstack1l1ll11ll_opy_(bstack11l1l1lll1l_opy_, bstack11l1ll1111l_opy_):
    proxies = {}
    global bstack11l1ll11l11_opy_
    if bstack11l1111_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨឞ") in globals():
        return bstack11l1ll11l11_opy_
    try:
        proxy = bstack11l1ll111l1_opy_(bstack11l1l1lll1l_opy_, bstack11l1ll1111l_opy_)
        if bstack11l1111_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨស") in proxy:
            proxies = {}
        elif bstack11l1111_opy_ (u"ࠢࡉࡖࡗࡔࠧហ") in proxy or bstack11l1111_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢឡ") in proxy or bstack11l1111_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣអ") in proxy:
            bstack11l1ll111ll_opy_ = proxy.split(bstack11l1111_opy_ (u"ࠥࠤࠧឣ"))
            if bstack11l1111_opy_ (u"ࠦ࠿࠵࠯ࠣឤ") in bstack11l1111_opy_ (u"ࠧࠨឥ").join(bstack11l1ll111ll_opy_[1:]):
                proxies = {
                    bstack11l1111_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬឦ"): bstack11l1111_opy_ (u"ࠢࠣឧ").join(bstack11l1ll111ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧឨ"): str(bstack11l1ll111ll_opy_[0]).lower() + bstack11l1111_opy_ (u"ࠤ࠽࠳࠴ࠨឩ") + bstack11l1111_opy_ (u"ࠥࠦឪ").join(bstack11l1ll111ll_opy_[1:])
                }
        elif bstack11l1111_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥឫ") in proxy:
            bstack11l1ll111ll_opy_ = proxy.split(bstack11l1111_opy_ (u"ࠧࠦࠢឬ"))
            if bstack11l1111_opy_ (u"ࠨ࠺࠰࠱ࠥឭ") in bstack11l1111_opy_ (u"ࠢࠣឮ").join(bstack11l1ll111ll_opy_[1:]):
                proxies = {
                    bstack11l1111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧឯ"): bstack11l1111_opy_ (u"ࠤࠥឰ").join(bstack11l1ll111ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l1111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩឱ"): bstack11l1111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧឲ") + bstack11l1111_opy_ (u"ࠧࠨឳ").join(bstack11l1ll111ll_opy_[1:])
                }
        else:
            proxies = {
                bstack11l1111_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ឴"): proxy
            }
    except Exception as e:
        print(bstack11l1111_opy_ (u"ࠢࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦ឵"), bstack11l1l1llll1_opy_.format(bstack11l1l1lll1l_opy_, str(e)))
    bstack11l1ll11l11_opy_ = proxies
    return proxies