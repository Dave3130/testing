# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll111111l_opy_, bstack1111lllll1_opy_, bstack1ll111ll_opy_, bstack1l1lll1111_opy_, \
    bstack11l1llllll1_opy_
from bstack_utils.measure import measure
def bstack11l1lll1l_opy_(bstack11ll11111ll_opy_):
    for driver in bstack11ll11111ll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l111llll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
def bstack1l1ll1l11l_opy_(driver, status, reason=bstack1lll11l_opy_ (u"࠭ࠧ᜚")):
    bstack111ll1l1_opy_ = Config.bstack111l1111_opy_()
    if bstack111ll1l1_opy_.bstack1llll1l1l_opy_():
        return
    bstack1l111l1ll1_opy_ = bstack111111ll11_opy_(bstack1lll11l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ᜛"), bstack1lll11l_opy_ (u"ࠨࠩ᜜"), status, reason, bstack1lll11l_opy_ (u"ࠩࠪ᜝"), bstack1lll11l_opy_ (u"ࠪࠫ᜞"))
    driver.execute_script(bstack1l111l1ll1_opy_)
@measure(event_name=EVENTS.bstack1l111llll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
def bstack11ll1l1l1l_opy_(page, status, reason=bstack1lll11l_opy_ (u"ࠫࠬᜟ")):
    try:
        if page is None:
            return
        bstack111ll1l1_opy_ = Config.bstack111l1111_opy_()
        if bstack111ll1l1_opy_.bstack1llll1l1l_opy_():
            return
        bstack1l111l1ll1_opy_ = bstack111111ll11_opy_(bstack1lll11l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᜠ"), bstack1lll11l_opy_ (u"࠭ࠧᜡ"), status, reason, bstack1lll11l_opy_ (u"ࠧࠨᜢ"), bstack1lll11l_opy_ (u"ࠨࠩᜣ"))
        page.evaluate(bstack1lll11l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᜤ"), bstack1l111l1ll1_opy_)
    except Exception as e:
        print(bstack1lll11l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࢁࡽࠣᜥ"), e)
def bstack111111ll11_opy_(type, name, status, reason, bstack1l11ll1l11_opy_, bstack111l11l11_opy_):
    bstack11111ll11l_opy_ = {
        bstack1lll11l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫᜦ"): type,
        bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜧ"): {}
    }
    if type == bstack1lll11l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨᜨ"):
        bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜩ")][bstack1lll11l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᜪ")] = bstack1l11ll1l11_opy_
        bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜫ")][bstack1lll11l_opy_ (u"ࠪࡨࡦࡺࡡࠨᜬ")] = json.dumps(str(bstack111l11l11_opy_))
    if type == bstack1lll11l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᜭ"):
        bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜮ")][bstack1lll11l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᜯ")] = name
    if type == bstack1lll11l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᜰ"):
        bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜱ")][bstack1lll11l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜲ")] = status
        if status == bstack1lll11l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᜳ") and str(reason) != bstack1lll11l_opy_ (u"᜴ࠦࠧ"):
            bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ᜵")][bstack1lll11l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭᜶")] = json.dumps(str(reason))
    bstack1l1111l1l_opy_ = bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ᜷").format(json.dumps(bstack11111ll11l_opy_))
    return bstack1l1111l1l_opy_
def bstack11llll11ll_opy_(url, config, logger, bstack1l1lllll1_opy_=False):
    hostname = bstack1111lllll1_opy_(url)
    is_private = bstack1l1lll1111_opy_(hostname)
    try:
        if is_private or bstack1l1lllll1_opy_:
            file_path = bstack11ll111111l_opy_(bstack1lll11l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᜸"), bstack1lll11l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨ᜹"), logger)
            if os.environ.get(bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨ᜺")) and eval(
                    os.environ.get(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩ᜻"))):
                return
            if (bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᜼") in config and not config[bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ᜽")]):
                os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬ᜾")] = str(True)
                bstack11l1lllllll_opy_ = {bstack1lll11l_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ᜿"): hostname}
                bstack11l1llllll1_opy_(bstack1lll11l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᝀ"), bstack1lll11l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨᝁ"), bstack11l1lllllll_opy_, logger)
    except Exception as e:
        pass
def bstack1ll1111l1_opy_(caps, bstack11l1lllll1l_opy_):
    if bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᝂ") in caps:
        caps[bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᝃ")][bstack1lll11l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬᝄ")] = True
        if bstack11l1lllll1l_opy_:
            caps[bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᝅ")][bstack1lll11l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᝆ")] = bstack11l1lllll1l_opy_
    else:
        caps[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧᝇ")] = True
        if bstack11l1lllll1l_opy_:
            caps[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᝈ")] = bstack11l1lllll1l_opy_
def bstack11ll1111111_opy_(bstack1l1lll1l_opy_):
    bstack11ll11111l1_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᝉ"), bstack1lll11l_opy_ (u"ࠬ࠭ᝊ"))
    if bstack11ll11111l1_opy_ == bstack1lll11l_opy_ (u"࠭ࠧᝋ") or bstack11ll11111l1_opy_ == bstack1lll11l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᝌ"):
        threading.current_thread().testStatus = bstack1l1lll1l_opy_
    else:
        if bstack1l1lll1l_opy_ == bstack1lll11l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᝍ"):
            threading.current_thread().testStatus = bstack1l1lll1l_opy_