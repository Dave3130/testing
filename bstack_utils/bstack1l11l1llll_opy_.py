# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll111l11l_opy_, bstack1lll1ll11l_opy_, bstack11lll111_opy_, bstack1l1l1l1l11_opy_, \
    bstack11ll111l1l1_opy_
from bstack_utils.measure import measure
def bstack1111l1l111_opy_(bstack11ll111l111_opy_):
    for driver in bstack11ll111l111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack111l1l111_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
def bstack1l1ll11l11_opy_(driver, status, reason=bstack1l1_opy_ (u"ࠬ࠭ᜋ")):
    bstack11l11111_opy_ = Config.bstack1111ll1l_opy_()
    if bstack11l11111_opy_.bstack1lll11l1l_opy_():
        return
    bstack11l1lll1l1_opy_ = bstack1111l1111_opy_(bstack1l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜌ"), bstack1l1_opy_ (u"ࠧࠨᜍ"), status, reason, bstack1l1_opy_ (u"ࠨࠩᜎ"), bstack1l1_opy_ (u"ࠩࠪᜏ"))
    driver.execute_script(bstack11l1lll1l1_opy_)
@measure(event_name=EVENTS.bstack111l1l111_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
def bstack1ll1ll1l11_opy_(page, status, reason=bstack1l1_opy_ (u"ࠪࠫᜐ")):
    try:
        if page is None:
            return
        bstack11l11111_opy_ = Config.bstack1111ll1l_opy_()
        if bstack11l11111_opy_.bstack1lll11l1l_opy_():
            return
        bstack11l1lll1l1_opy_ = bstack1111l1111_opy_(bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᜑ"), bstack1l1_opy_ (u"ࠬ࠭ᜒ"), status, reason, bstack1l1_opy_ (u"࠭ࠧᜓ"), bstack1l1_opy_ (u"ࠧࠨ᜔"))
        page.evaluate(bstack1l1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ᜕"), bstack11l1lll1l1_opy_)
    except Exception as e:
        print(bstack1l1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࢀࢃࠢ᜖"), e)
def bstack1111l1111_opy_(type, name, status, reason, bstack1l1111ll1_opy_, bstack11l1lll11_opy_):
    bstack11lll1l1l_opy_ = {
        bstack1l1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ᜗"): type,
        bstack1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ᜘"): {}
    }
    if type == bstack1l1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ᜙"):
        bstack11lll1l1l_opy_[bstack1l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ᜚")][bstack1l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭᜛")] = bstack1l1111ll1_opy_
        bstack11lll1l1l_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ᜜")][bstack1l1_opy_ (u"ࠩࡧࡥࡹࡧࠧ᜝")] = json.dumps(str(bstack11l1lll11_opy_))
    if type == bstack1l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ᜞"):
        bstack11lll1l1l_opy_[bstack1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜟ")][bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᜠ")] = name
    if type == bstack1l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜡ"):
        bstack11lll1l1l_opy_[bstack1l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜢ")][bstack1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜣ")] = status
        if status == bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᜤ") and str(reason) != bstack1l1_opy_ (u"ࠥࠦᜥ"):
            bstack11lll1l1l_opy_[bstack1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜦ")][bstack1l1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᜧ")] = json.dumps(str(reason))
    bstack11111l1ll1_opy_ = bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᜨ").format(json.dumps(bstack11lll1l1l_opy_))
    return bstack11111l1ll1_opy_
def bstack11llll1l11_opy_(url, config, logger, bstack1llll1l111_opy_=False):
    hostname = bstack1lll1ll11l_opy_(url)
    is_private = bstack1l1l1l1l11_opy_(hostname)
    try:
        if is_private or bstack1llll1l111_opy_:
            file_path = bstack11ll111l11l_opy_(bstack1l1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᜩ"), bstack1l1_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᜪ"), logger)
            if os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᜫ")) and eval(
                    os.environ.get(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜬ"))):
                return
            if (bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᜭ") in config and not config[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩᜮ")]):
                os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᜯ")] = str(True)
                bstack11ll1111l11_opy_ = {bstack1l1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩᜰ"): hostname}
                bstack11ll111l1l1_opy_(bstack1l1_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᜱ"), bstack1l1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧᜲ"), bstack11ll1111l11_opy_, logger)
    except Exception as e:
        pass
def bstack11ll111l1l_opy_(caps, bstack11ll1111l1l_opy_):
    if bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᜳ") in caps:
        caps[bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷ᜴ࠬ")][bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫ᜵")] = True
        if bstack11ll1111l1l_opy_:
            caps[bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᜶")][bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᜷")] = bstack11ll1111l1l_opy_
    else:
        caps[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭᜸")] = True
        if bstack11ll1111l1l_opy_:
            caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ᜹")] = bstack11ll1111l1l_opy_
def bstack11ll1111ll1_opy_(bstack1lll11ll_opy_):
    bstack11ll1111lll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧ᜺"), bstack1l1_opy_ (u"ࠫࠬ᜻"))
    if bstack11ll1111lll_opy_ == bstack1l1_opy_ (u"ࠬ࠭᜼") or bstack11ll1111lll_opy_ == bstack1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ᜽"):
        threading.current_thread().testStatus = bstack1lll11ll_opy_
    else:
        if bstack1lll11ll_opy_ == bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᜾"):
            threading.current_thread().testStatus = bstack1lll11ll_opy_