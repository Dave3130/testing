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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll11l111l_opy_, bstack1ll1l111l_opy_, bstack11lll111_opy_, bstack1l1ll11ll1_opy_, \
    bstack11ll111l1ll_opy_
from bstack_utils.measure import measure
def bstack111l1l1l1l_opy_(bstack11ll111ll11_opy_):
    for driver in bstack11ll111ll11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l11l11l1_opy_, stage=STAGE.bstack11l1lllll_opy_)
def bstack11ll1111ll_opy_(driver, status, reason=bstack11l1l11_opy_ (u"ࠫࠬᛮ")):
    bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
    if bstack111111ll_opy_.bstack11l11ll1_opy_():
        return
    bstack1l1ll1111l_opy_ = bstack1lll1ll11l_opy_(bstack11l1l11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᛯ"), bstack11l1l11_opy_ (u"࠭ࠧᛰ"), status, reason, bstack11l1l11_opy_ (u"ࠧࠨᛱ"), bstack11l1l11_opy_ (u"ࠨࠩᛲ"))
    driver.execute_script(bstack1l1ll1111l_opy_)
@measure(event_name=EVENTS.bstack1l11l11l1_opy_, stage=STAGE.bstack11l1lllll_opy_)
def bstack1ll1lllll_opy_(page, status, reason=bstack11l1l11_opy_ (u"ࠩࠪᛳ")):
    try:
        if page is None:
            return
        bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
        if bstack111111ll_opy_.bstack11l11ll1_opy_():
            return
        bstack1l1ll1111l_opy_ = bstack1lll1ll11l_opy_(bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᛴ"), bstack11l1l11_opy_ (u"ࠫࠬᛵ"), status, reason, bstack11l1l11_opy_ (u"ࠬ࠭ᛶ"), bstack11l1l11_opy_ (u"࠭ࠧᛷ"))
        page.evaluate(bstack11l1l11_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᛸ"), bstack1l1ll1111l_opy_)
    except Exception as e:
        print(bstack11l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨ᛹"), e)
def bstack1lll1ll11l_opy_(type, name, status, reason, bstack1l11l1l111_opy_, bstack1l1l1ll11_opy_):
    bstack11ll11l11_opy_ = {
        bstack11l1l11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ᛺"): type,
        bstack11l1l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭᛻"): {}
    }
    if type == bstack11l1l11_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭᛼"):
        bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ᛽")][bstack11l1l11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ᛾")] = bstack1l11l1l111_opy_
        bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ᛿")][bstack11l1l11_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᜀ")] = json.dumps(str(bstack1l1l1ll11_opy_))
    if type == bstack11l1l11_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᜁ"):
        bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜂ")][bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᜃ")] = name
    if type == bstack11l1l11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᜄ"):
        bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜅ")][bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᜆ")] = status
        if status == bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᜇ") and str(reason) != bstack11l1l11_opy_ (u"ࠤࠥᜈ"):
            bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜉ")][bstack11l1l11_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᜊ")] = json.dumps(str(reason))
    bstack11l1l1l111_opy_ = bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᜋ").format(json.dumps(bstack11ll11l11_opy_))
    return bstack11l1l1l111_opy_
def bstack11llll1ll1_opy_(url, config, logger, bstack11lll1lll_opy_=False):
    hostname = bstack1ll1l111l_opy_(url)
    is_private = bstack1l1ll11ll1_opy_(hostname)
    try:
        if is_private or bstack11lll1lll_opy_:
            file_path = bstack11ll11l111l_opy_(bstack11l1l11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᜌ"), bstack11l1l11_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᜍ"), logger)
            if os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᜎ")) and eval(
                    os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᜏ"))):
                return
            if (bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᜐ") in config and not config[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᜑ")]):
                os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᜒ")] = str(True)
                bstack11ll111llll_opy_ = {bstack11l1l11_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨᜓ"): hostname}
                bstack11ll111l1ll_opy_(bstack11l1l11_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ᜔࠭"), bstack11l1l11_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ᜕࠭"), bstack11ll111llll_opy_, logger)
    except Exception as e:
        pass
def bstack11l1llllll_opy_(caps, bstack11ll111lll1_opy_):
    if bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ᜖") in caps:
        caps[bstack11l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ᜗")][bstack11l1l11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ᜘")] = True
        if bstack11ll111lll1_opy_:
            caps[bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᜙")][bstack11l1l11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ᜚")] = bstack11ll111lll1_opy_
    else:
        caps[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬ᜛")] = True
        if bstack11ll111lll1_opy_:
            caps[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᜜")] = bstack11ll111lll1_opy_
def bstack11ll111ll1l_opy_(bstack1l1111l1_opy_):
    bstack11ll11l1111_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭᜝"), bstack11l1l11_opy_ (u"ࠪࠫ᜞"))
    if bstack11ll11l1111_opy_ == bstack11l1l11_opy_ (u"ࠫࠬᜟ") or bstack11ll11l1111_opy_ == bstack11l1l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᜠ"):
        threading.current_thread().testStatus = bstack1l1111l1_opy_
    else:
        if bstack1l1111l1_opy_ == bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᜡ"):
            threading.current_thread().testStatus = bstack1l1111l1_opy_