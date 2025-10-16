# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1lll111l_opy_
bstack1111ll11_opy_ = Config.bstack1llll11l1_opy_()
def bstack11l1lll11ll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1lll1lll_opy_(bstack11l1lll1ll1_opy_, bstack11l1llll111_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1lll1ll1_opy_):
        with open(bstack11l1lll1ll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1lll11ll_opy_(bstack11l1lll1ll1_opy_):
        pac = get_pac(url=bstack11l1lll1ll1_opy_)
    else:
        raise Exception(bstack1ll11_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬᝑ").format(bstack11l1lll1ll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1ll11_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢᝒ"), 80))
        bstack11l1lll1l1l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1lll1l1l_opy_ = bstack1ll11_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨᝓ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1llll111_opy_, bstack11l1lll1l1l_opy_)
    return proxy_url
def bstack111l111l1_opy_(config):
    return bstack1ll11_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ᝔") in config or bstack1ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭᝕") in config
def bstack11l1l11l11_opy_(config):
    if not bstack111l111l1_opy_(config):
        return
    if config.get(bstack1ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᝖")):
        return config.get(bstack1ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ᝗"))
    if config.get(bstack1ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ᝘")):
        return config.get(bstack1ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ᝙"))
def bstack1111l1ll1_opy_(config, bstack11l1llll111_opy_):
    proxy = bstack11l1l11l11_opy_(config)
    proxies = {}
    if config.get(bstack1ll11_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ᝚")) or config.get(bstack1ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᝛")):
        if proxy.endswith(bstack1ll11_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ᝜")):
            proxies = bstack1ll1111l1_opy_(proxy, bstack11l1llll111_opy_)
        else:
            proxies = {
                bstack1ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩ᝝"): proxy
            }
    bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡖࡩࡹࡺࡩ࡯ࡩࡶࠫ᝞"), proxies)
    return proxies
def bstack1ll1111l1_opy_(bstack11l1lll1ll1_opy_, bstack11l1llll111_opy_):
    proxies = {}
    global bstack11l1lll11l1_opy_
    if bstack1ll11_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨ᝟") in globals():
        return bstack11l1lll11l1_opy_
    try:
        proxy = bstack11l1lll1lll_opy_(bstack11l1lll1ll1_opy_, bstack11l1llll111_opy_)
        if bstack1ll11_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨᝠ") in proxy:
            proxies = {}
        elif bstack1ll11_opy_ (u"ࠢࡉࡖࡗࡔࠧᝡ") in proxy or bstack1ll11_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢᝢ") in proxy or bstack1ll11_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣᝣ") in proxy:
            bstack11l1lll1l11_opy_ = proxy.split(bstack1ll11_opy_ (u"ࠥࠤࠧᝤ"))
            if bstack1ll11_opy_ (u"ࠦ࠿࠵࠯ࠣᝥ") in bstack1ll11_opy_ (u"ࠧࠨᝦ").join(bstack11l1lll1l11_opy_[1:]):
                proxies = {
                    bstack1ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᝧ"): bstack1ll11_opy_ (u"ࠢࠣᝨ").join(bstack11l1lll1l11_opy_[1:])
                }
            else:
                proxies = {
                    bstack1ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᝩ"): str(bstack11l1lll1l11_opy_[0]).lower() + bstack1ll11_opy_ (u"ࠤ࠽࠳࠴ࠨᝪ") + bstack1ll11_opy_ (u"ࠥࠦᝫ").join(bstack11l1lll1l11_opy_[1:])
                }
        elif bstack1ll11_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥᝬ") in proxy:
            bstack11l1lll1l11_opy_ = proxy.split(bstack1ll11_opy_ (u"ࠧࠦࠢ᝭"))
            if bstack1ll11_opy_ (u"ࠨ࠺࠰࠱ࠥᝮ") in bstack1ll11_opy_ (u"ࠢࠣᝯ").join(bstack11l1lll1l11_opy_[1:]):
                proxies = {
                    bstack1ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᝰ"): bstack1ll11_opy_ (u"ࠤࠥ᝱").join(bstack11l1lll1l11_opy_[1:])
                }
            else:
                proxies = {
                    bstack1ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᝲ"): bstack1ll11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᝳ") + bstack1ll11_opy_ (u"ࠧࠨ᝴").join(bstack11l1lll1l11_opy_[1:])
                }
        else:
            proxies = {
                bstack1ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ᝵"): proxy
            }
    except Exception as e:
        print(bstack1ll11_opy_ (u"ࠢࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠦ᝶"), bstack11l1lll111l_opy_.format(bstack11l1lll1ll1_opy_, str(e)))
    bstack11l1lll11l1_opy_ = proxies
    return proxies