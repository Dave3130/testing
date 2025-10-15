# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll111lll1_opy_, bstack1l111l11l1_opy_, bstack1l1l1l1l_opy_, bstack11llllll11_opy_, \
    bstack11ll111ll11_opy_
from bstack_utils.measure import measure
def bstack1l1l1ll11_opy_(bstack11ll111ll1l_opy_):
    for driver in bstack11ll111ll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11llll1l1_opy_, stage=STAGE.bstack11lll11ll_opy_)
def bstack1ll11111l_opy_(driver, status, reason=bstack1ll1l_opy_ (u"࠭ࠧᛰ")):
    bstack111111ll_opy_ = Config.bstack111l1ll1_opy_()
    if bstack111111ll_opy_.bstack1lll1l1ll_opy_():
        return
    bstack11111l1lll_opy_ = bstack11l11111l_opy_(bstack1ll1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᛱ"), bstack1ll1l_opy_ (u"ࠨࠩᛲ"), status, reason, bstack1ll1l_opy_ (u"ࠩࠪᛳ"), bstack1ll1l_opy_ (u"ࠪࠫᛴ"))
    driver.execute_script(bstack11111l1lll_opy_)
@measure(event_name=EVENTS.bstack11llll1l1_opy_, stage=STAGE.bstack11lll11ll_opy_)
def bstack1ll1l1ll1_opy_(page, status, reason=bstack1ll1l_opy_ (u"ࠫࠬᛵ")):
    try:
        if page is None:
            return
        bstack111111ll_opy_ = Config.bstack111l1ll1_opy_()
        if bstack111111ll_opy_.bstack1lll1l1ll_opy_():
            return
        bstack11111l1lll_opy_ = bstack11l11111l_opy_(bstack1ll1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᛶ"), bstack1ll1l_opy_ (u"࠭ࠧᛷ"), status, reason, bstack1ll1l_opy_ (u"ࠧࠨᛸ"), bstack1ll1l_opy_ (u"ࠨࠩ᛹"))
        page.evaluate(bstack1ll1l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ᛺"), bstack11111l1lll_opy_)
    except Exception as e:
        print(bstack1ll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࢁࡽࠣ᛻"), e)
def bstack11l11111l_opy_(type, name, status, reason, bstack1ll11l1111_opy_, bstack1ll111l11_opy_):
    bstack111llll1l1_opy_ = {
        bstack1ll1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ᛼"): type,
        bstack1ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ᛽"): {}
    }
    if type == bstack1ll1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ᛾"):
        bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ᛿")][bstack1ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᜀ")] = bstack1ll11l1111_opy_
        bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜁ")][bstack1ll1l_opy_ (u"ࠪࡨࡦࡺࡡࠨᜂ")] = json.dumps(str(bstack1ll111l11_opy_))
    if type == bstack1ll1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᜃ"):
        bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜄ")][bstack1ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᜅ")] = name
    if type == bstack1ll1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᜆ"):
        bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜇ")][bstack1ll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜈ")] = status
        if status == bstack1ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᜉ") and str(reason) != bstack1ll1l_opy_ (u"ࠦࠧᜊ"):
            bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜋ")][bstack1ll1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᜌ")] = json.dumps(str(reason))
    bstack1l1l1ll1ll_opy_ = bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬᜍ").format(json.dumps(bstack111llll1l1_opy_))
    return bstack1l1l1ll1ll_opy_
def bstack1l11l1l11l_opy_(url, config, logger, bstack11ll111l1_opy_=False):
    hostname = bstack1l111l11l1_opy_(url)
    is_private = bstack11llllll11_opy_(hostname)
    try:
        if is_private or bstack11ll111l1_opy_:
            file_path = bstack11ll111lll1_opy_(bstack1ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᜎ"), bstack1ll1l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᜏ"), logger)
            if os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜐ")) and eval(
                    os.environ.get(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᜑ"))):
                return
            if (bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᜒ") in config and not config[bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᜓ")]):
                os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖ᜔ࠬ")] = str(True)
                bstack11ll111l1ll_opy_ = {bstack1ll1l_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧ᜕ࠪ"): hostname}
                bstack11ll111ll11_opy_(bstack1ll1l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨ᜖"), bstack1ll1l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨ᜗"), bstack11ll111l1ll_opy_, logger)
    except Exception as e:
        pass
def bstack11l1l1llll_opy_(caps, bstack11ll11l1111_opy_):
    if bstack1ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᜘") in caps:
        caps[bstack1ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᜙")][bstack1ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ᜚")] = True
        if bstack11ll11l1111_opy_:
            caps[bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᜛")][bstack1ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ᜜")] = bstack11ll11l1111_opy_
    else:
        caps[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧ᜝")] = True
        if bstack11ll11l1111_opy_:
            caps[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ᜞")] = bstack11ll11l1111_opy_
def bstack11ll11l111l_opy_(bstack1l1l11ll_opy_):
    bstack11ll111llll_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᜟ"), bstack1ll1l_opy_ (u"ࠬ࠭ᜠ"))
    if bstack11ll111llll_opy_ == bstack1ll1l_opy_ (u"࠭ࠧᜡ") or bstack11ll111llll_opy_ == bstack1ll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᜢ"):
        threading.current_thread().testStatus = bstack1l1l11ll_opy_
    else:
        if bstack1l1l11ll_opy_ == bstack1ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᜣ"):
            threading.current_thread().testStatus = bstack1l1l11ll_opy_