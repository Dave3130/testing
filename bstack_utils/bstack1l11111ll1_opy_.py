# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll111lll1_opy_, bstack111ll11l1l_opy_, bstack1lll111l_opy_, bstack111lll11l1_opy_, \
    bstack11ll11l111l_opy_
from bstack_utils.measure import measure
def bstack1ll11l1l1_opy_(bstack11ll11l1111_opy_):
    for driver in bstack11ll11l1111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l1ll1l11_opy_, stage=STAGE.bstack11l11ll11_opy_)
def bstack1ll111l1ll_opy_(driver, status, reason=bstack111111l_opy_ (u"ࠨࠩ᛫")):
    bstack11111lll_opy_ = Config.bstack111l111l_opy_()
    if bstack11111lll_opy_.bstack11l1l11l_opy_():
        return
    bstack11ll111lll_opy_ = bstack111lllllll_opy_(bstack111111l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬ᛬"), bstack111111l_opy_ (u"ࠪࠫ᛭"), status, reason, bstack111111l_opy_ (u"ࠫࠬᛮ"), bstack111111l_opy_ (u"ࠬ࠭ᛯ"))
    driver.execute_script(bstack11ll111lll_opy_)
@measure(event_name=EVENTS.bstack1l1ll1l11_opy_, stage=STAGE.bstack11l11ll11_opy_)
def bstack111ll1lll_opy_(page, status, reason=bstack111111l_opy_ (u"࠭ࠧᛰ")):
    try:
        if page is None:
            return
        bstack11111lll_opy_ = Config.bstack111l111l_opy_()
        if bstack11111lll_opy_.bstack11l1l11l_opy_():
            return
        bstack11ll111lll_opy_ = bstack111lllllll_opy_(bstack111111l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᛱ"), bstack111111l_opy_ (u"ࠨࠩᛲ"), status, reason, bstack111111l_opy_ (u"ࠩࠪᛳ"), bstack111111l_opy_ (u"ࠪࠫᛴ"))
        page.evaluate(bstack111111l_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᛵ"), bstack11ll111lll_opy_)
    except Exception as e:
        print(bstack111111l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡼࡿࠥᛶ"), e)
def bstack111lllllll_opy_(type, name, status, reason, bstack1ll111lll1_opy_, bstack1l1l1lll1_opy_):
    bstack111ll1l11l_opy_ = {
        bstack111111l_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ᛷ"): type,
        bstack111111l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᛸ"): {}
    }
    if type == bstack111111l_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ᛹"):
        bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ᛺")][bstack111111l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ᛻")] = bstack1ll111lll1_opy_
        bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ᛼")][bstack111111l_opy_ (u"ࠬࡪࡡࡵࡣࠪ᛽")] = json.dumps(str(bstack1l1l1lll1_opy_))
    if type == bstack111111l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ᛾"):
        bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ᛿")][bstack111111l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᜀ")] = name
    if type == bstack111111l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᜁ"):
        bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜂ")][bstack111111l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᜃ")] = status
        if status == bstack111111l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᜄ") and str(reason) != bstack111111l_opy_ (u"ࠨࠢᜅ"):
            bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜆ")][bstack111111l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᜇ")] = json.dumps(str(reason))
    bstack11l1ll1111_opy_ = bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧᜈ").format(json.dumps(bstack111ll1l11l_opy_))
    return bstack11l1ll1111_opy_
def bstack1111l1l11_opy_(url, config, logger, bstack11ll1l1l11_opy_=False):
    hostname = bstack111ll11l1l_opy_(url)
    is_private = bstack111lll11l1_opy_(hostname)
    try:
        if is_private or bstack11ll1l1l11_opy_:
            file_path = bstack11ll111lll1_opy_(bstack111111l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᜉ"), bstack111111l_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪᜊ"), logger)
            if os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᜋ")) and eval(
                    os.environ.get(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᜌ"))):
                return
            if (bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᜍ") in config and not config[bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᜎ")]):
                os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᜏ")] = str(True)
                bstack11ll111l1ll_opy_ = {bstack111111l_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬᜐ"): hostname}
                bstack11ll11l111l_opy_(bstack111111l_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪᜑ"), bstack111111l_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪᜒ"), bstack11ll111l1ll_opy_, logger)
    except Exception as e:
        pass
def bstack1lll1llll1_opy_(caps, bstack11ll111llll_opy_):
    if bstack111111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᜓ") in caps:
        caps[bstack111111l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᜔")][bstack111111l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲ᜕ࠧ")] = True
        if bstack11ll111llll_opy_:
            caps[bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ᜖")][bstack111111l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ᜗")] = bstack11ll111llll_opy_
    else:
        caps[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩ᜘")] = True
        if bstack11ll111llll_opy_:
            caps[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭᜙")] = bstack11ll111llll_opy_
def bstack11ll111ll1l_opy_(bstack1lll1lll_opy_):
    bstack11ll111ll11_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪ᜚"), bstack111111l_opy_ (u"ࠧࠨ᜛"))
    if bstack11ll111ll11_opy_ == bstack111111l_opy_ (u"ࠨࠩ᜜") or bstack11ll111ll11_opy_ == bstack111111l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ᜝"):
        threading.current_thread().testStatus = bstack1lll1lll_opy_
    else:
        if bstack1lll1lll_opy_ == bstack111111l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᜞"):
            threading.current_thread().testStatus = bstack1lll1lll_opy_