# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1111ll1_opy_, bstack11llllll11_opy_, bstack1ll11l1l_opy_, bstack11l1l1l111_opy_, \
    bstack11ll1111l1l_opy_
from bstack_utils.measure import measure
def bstack1l1ll111l_opy_(bstack11ll111l1l1_opy_):
    for driver in bstack11ll111l1l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l1l111l11_opy_, stage=STAGE.bstack1ll1lllll_opy_)
def bstack11l11ll11l_opy_(driver, status, reason=bstack11l11l1_opy_ (u"ࠬ࠭ᜋ")):
    bstack11111111_opy_ = Config.bstack1llll1ll1_opy_()
    if bstack11111111_opy_.bstack111l1111_opy_():
        return
    bstack1l11l1llll_opy_ = bstack1ll11l11l1_opy_(bstack11l11l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜌ"), bstack11l11l1_opy_ (u"ࠧࠨᜍ"), status, reason, bstack11l11l1_opy_ (u"ࠨࠩᜎ"), bstack11l11l1_opy_ (u"ࠩࠪᜏ"))
    driver.execute_script(bstack1l11l1llll_opy_)
@measure(event_name=EVENTS.bstack1l1l111l11_opy_, stage=STAGE.bstack1ll1lllll_opy_)
def bstack11l111l11_opy_(page, status, reason=bstack11l11l1_opy_ (u"ࠪࠫᜐ")):
    try:
        if page is None:
            return
        bstack11111111_opy_ = Config.bstack1llll1ll1_opy_()
        if bstack11111111_opy_.bstack111l1111_opy_():
            return
        bstack1l11l1llll_opy_ = bstack1ll11l11l1_opy_(bstack11l11l1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᜑ"), bstack11l11l1_opy_ (u"ࠬ࠭ᜒ"), status, reason, bstack11l11l1_opy_ (u"࠭ࠧᜓ"), bstack11l11l1_opy_ (u"ࠧࠨ᜔"))
        page.evaluate(bstack11l11l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ᜕"), bstack1l11l1llll_opy_)
    except Exception as e:
        print(bstack11l11l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࢀࢃࠢ᜖"), e)
def bstack1ll11l11l1_opy_(type, name, status, reason, bstack11l11111ll_opy_, bstack1lll11ll1l_opy_):
    bstack111ll11l1_opy_ = {
        bstack11l11l1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ᜗"): type,
        bstack11l11l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ᜘"): {}
    }
    if type == bstack11l11l1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ᜙"):
        bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ᜚")][bstack11l11l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭᜛")] = bstack11l11111ll_opy_
        bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ᜜")][bstack11l11l1_opy_ (u"ࠩࡧࡥࡹࡧࠧ᜝")] = json.dumps(str(bstack1lll11ll1l_opy_))
    if type == bstack11l11l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ᜞"):
        bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜟ")][bstack11l11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᜠ")] = name
    if type == bstack11l11l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜡ"):
        bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜢ")][bstack11l11l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜣ")] = status
        if status == bstack11l11l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᜤ") and str(reason) != bstack11l11l1_opy_ (u"ࠥࠦᜥ"):
            bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜦ")][bstack11l11l1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᜧ")] = json.dumps(str(reason))
    bstack11lll1l1l1_opy_ = bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᜨ").format(json.dumps(bstack111ll11l1_opy_))
    return bstack11lll1l1l1_opy_
def bstack1l1l11llll_opy_(url, config, logger, bstack1lll1l11ll_opy_=False):
    hostname = bstack11llllll11_opy_(url)
    is_private = bstack11l1l1l111_opy_(hostname)
    try:
        if is_private or bstack1lll1l11ll_opy_:
            file_path = bstack11ll1111ll1_opy_(bstack11l11l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᜩ"), bstack11l11l1_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᜪ"), logger)
            if os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᜫ")) and eval(
                    os.environ.get(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜬ"))):
                return
            if (bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᜭ") in config and not config[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᜮ")]):
                os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᜯ")] = str(True)
                bstack11ll1111lll_opy_ = {bstack11l11l1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩᜰ"): hostname}
                bstack11ll1111l1l_opy_(bstack11l11l1_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᜱ"), bstack11l11l1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧᜲ"), bstack11ll1111lll_opy_, logger)
    except Exception as e:
        pass
def bstack1lllll11ll_opy_(caps, bstack11ll111l11l_opy_):
    if bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᜳ") in caps:
        caps[bstack11l11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷ᜴ࠬ")][bstack11l11l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫ᜵")] = True
        if bstack11ll111l11l_opy_:
            caps[bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᜶")][bstack11l11l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᜷")] = bstack11ll111l11l_opy_
    else:
        caps[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭᜸")] = True
        if bstack11ll111l11l_opy_:
            caps[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ᜹")] = bstack11ll111l11l_opy_
def bstack11ll1111l11_opy_(bstack1l1111l1_opy_):
    bstack11ll111l111_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧ᜺"), bstack11l11l1_opy_ (u"ࠫࠬ᜻"))
    if bstack11ll111l111_opy_ == bstack11l11l1_opy_ (u"ࠬ࠭᜼") or bstack11ll111l111_opy_ == bstack11l11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ᜽"):
        threading.current_thread().testStatus = bstack1l1111l1_opy_
    else:
        if bstack1l1111l1_opy_ == bstack11l11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᜾"):
            threading.current_thread().testStatus = bstack1l1111l1_opy_