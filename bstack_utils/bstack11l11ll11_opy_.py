# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll11l11ll_opy_, bstack1111l1ll11_opy_, bstack1llll11l_opy_, bstack1l1ll111l1_opy_, \
    bstack11ll111ll1l_opy_
from bstack_utils.measure import measure
def bstack1l1l11111_opy_(bstack11ll111llll_opy_):
    for driver in bstack11ll111llll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l11ll1ll_opy_, stage=STAGE.bstack11ll111111_opy_)
def bstack11111ll111_opy_(driver, status, reason=bstack1l_opy_ (u"ࠧࠨᛸ")):
    bstack1lll1ll1l_opy_ = Config.bstack1llll11ll_opy_()
    if bstack1lll1ll1l_opy_.bstack1llll1l11_opy_():
        return
    bstack111lll1ll_opy_ = bstack111ll11l11_opy_(bstack1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ᛹"), bstack1l_opy_ (u"ࠩࠪ᛺"), status, reason, bstack1l_opy_ (u"ࠪࠫ᛻"), bstack1l_opy_ (u"ࠫࠬ᛼"))
    driver.execute_script(bstack111lll1ll_opy_)
@measure(event_name=EVENTS.bstack1l11ll1ll_opy_, stage=STAGE.bstack11ll111111_opy_)
def bstack111llll1ll_opy_(page, status, reason=bstack1l_opy_ (u"ࠬ࠭᛽")):
    try:
        if page is None:
            return
        bstack1lll1ll1l_opy_ = Config.bstack1llll11ll_opy_()
        if bstack1lll1ll1l_opy_.bstack1llll1l11_opy_():
            return
        bstack111lll1ll_opy_ = bstack111ll11l11_opy_(bstack1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ᛾"), bstack1l_opy_ (u"ࠧࠨ᛿"), status, reason, bstack1l_opy_ (u"ࠨࠩᜀ"), bstack1l_opy_ (u"ࠩࠪᜁ"))
        page.evaluate(bstack1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᜂ"), bstack111lll1ll_opy_)
    except Exception as e:
        print(bstack1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡻࡾࠤᜃ"), e)
def bstack111ll11l11_opy_(type, name, status, reason, bstack1l111l11l1_opy_, bstack11l111lll_opy_):
    bstack1ll1l11l1_opy_ = {
        bstack1l_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬᜄ"): type,
        bstack1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜅ"): {}
    }
    if type == bstack1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩᜆ"):
        bstack1ll1l11l1_opy_[bstack1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜇ")][bstack1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᜈ")] = bstack1l111l11l1_opy_
        bstack1ll1l11l1_opy_[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜉ")][bstack1l_opy_ (u"ࠫࡩࡧࡴࡢࠩᜊ")] = json.dumps(str(bstack11l111lll_opy_))
    if type == bstack1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᜋ"):
        bstack1ll1l11l1_opy_[bstack1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜌ")][bstack1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᜍ")] = name
    if type == bstack1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫᜎ"):
        bstack1ll1l11l1_opy_[bstack1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜏ")][bstack1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᜐ")] = status
        if status == bstack1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᜑ") and str(reason) != bstack1l_opy_ (u"ࠧࠨᜒ"):
            bstack1ll1l11l1_opy_[bstack1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜓ")][bstack1l_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴ᜔ࠧ")] = json.dumps(str(reason))
    bstack11111l111_opy_ = bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ᜕࠭").format(json.dumps(bstack1ll1l11l1_opy_))
    return bstack11111l111_opy_
def bstack1l1lll1111_opy_(url, config, logger, bstack1l1lll11l1_opy_=False):
    hostname = bstack1111l1ll11_opy_(url)
    is_private = bstack1l1ll111l1_opy_(hostname)
    try:
        if is_private or bstack1l1lll11l1_opy_:
            file_path = bstack11ll11l11ll_opy_(bstack1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ᜖"), bstack1l_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩ᜗"), logger)
            if os.environ.get(bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩ᜘")) and eval(
                    os.environ.get(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ᜙"))):
                return
            if (bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ᜚") in config and not config[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ᜛")]):
                os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭᜜")] = str(True)
                bstack11ll11l11l1_opy_ = {bstack1l_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ᜝"): hostname}
                bstack11ll111ll1l_opy_(bstack1l_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩ᜞"), bstack1l_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩᜟ"), bstack11ll11l11l1_opy_, logger)
    except Exception as e:
        pass
def bstack1l11llllll_opy_(caps, bstack11ll111lll1_opy_):
    if bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᜠ") in caps:
        caps[bstack1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᜡ")][bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ᜢ")] = True
        if bstack11ll111lll1_opy_:
            caps[bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᜣ")][bstack1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᜤ")] = bstack11ll111lll1_opy_
    else:
        caps[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨᜥ")] = True
        if bstack11ll111lll1_opy_:
            caps[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᜦ")] = bstack11ll111lll1_opy_
def bstack11ll11l111l_opy_(bstack1ll11ll1_opy_):
    bstack11ll11l1111_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩᜧ"), bstack1l_opy_ (u"࠭ࠧᜨ"))
    if bstack11ll11l1111_opy_ == bstack1l_opy_ (u"ࠧࠨᜩ") or bstack11ll11l1111_opy_ == bstack1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᜪ"):
        threading.current_thread().testStatus = bstack1ll11ll1_opy_
    else:
        if bstack1ll11ll1_opy_ == bstack1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᜫ"):
            threading.current_thread().testStatus = bstack1ll11ll1_opy_