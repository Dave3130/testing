# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll11111l1_opy_, bstack11lll11l1_opy_, bstack1l1l11l1_opy_, bstack11llll11ll_opy_, \
    bstack11ll1111ll1_opy_
from bstack_utils.measure import measure
def bstack111llll1l1_opy_(bstack11ll1111l11_opy_):
    for driver in bstack11ll1111l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11ll1ll11l_opy_, stage=STAGE.bstack1ll1111l1_opy_)
def bstack1ll1111111_opy_(driver, status, reason=bstack11ll_opy_ (u"࠭ࠧ᜚")):
    bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
    if bstack1111l111_opy_.bstack111111ll_opy_():
        return
    bstack1lll1l1l1l_opy_ = bstack11l1l1l11_opy_(bstack11ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ᜛"), bstack11ll_opy_ (u"ࠨࠩ᜜"), status, reason, bstack11ll_opy_ (u"ࠩࠪ᜝"), bstack11ll_opy_ (u"ࠪࠫ᜞"))
    driver.execute_script(bstack1lll1l1l1l_opy_)
@measure(event_name=EVENTS.bstack11ll1ll11l_opy_, stage=STAGE.bstack1ll1111l1_opy_)
def bstack111l1l1lll_opy_(page, status, reason=bstack11ll_opy_ (u"ࠫࠬᜟ")):
    try:
        if page is None:
            return
        bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
        if bstack1111l111_opy_.bstack111111ll_opy_():
            return
        bstack1lll1l1l1l_opy_ = bstack11l1l1l11_opy_(bstack11ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᜠ"), bstack11ll_opy_ (u"࠭ࠧᜡ"), status, reason, bstack11ll_opy_ (u"ࠧࠨᜢ"), bstack11ll_opy_ (u"ࠨࠩᜣ"))
        page.evaluate(bstack11ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᜤ"), bstack1lll1l1l1l_opy_)
    except Exception as e:
        print(bstack11ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࢁࡽࠣᜥ"), e)
def bstack11l1l1l11_opy_(type, name, status, reason, bstack11l111ll1_opy_, bstack1l1l11ll11_opy_):
    bstack1ll1111ll_opy_ = {
        bstack11ll_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫᜦ"): type,
        bstack11ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜧ"): {}
    }
    if type == bstack11ll_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨᜨ"):
        bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜩ")][bstack11ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᜪ")] = bstack11l111ll1_opy_
        bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜫ")][bstack11ll_opy_ (u"ࠪࡨࡦࡺࡡࠨᜬ")] = json.dumps(str(bstack1l1l11ll11_opy_))
    if type == bstack11ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᜭ"):
        bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜮ")][bstack11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᜯ")] = name
    if type == bstack11ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᜰ"):
        bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜱ")][bstack11ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜲ")] = status
        if status == bstack11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᜳ") and str(reason) != bstack11ll_opy_ (u"᜴ࠦࠧ"):
            bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ᜵")][bstack11ll_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭᜶")] = json.dumps(str(reason))
    bstack11ll11l111_opy_ = bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ᜷").format(json.dumps(bstack1ll1111ll_opy_))
    return bstack11ll11l111_opy_
def bstack1111l1lll_opy_(url, config, logger, bstack111l11lll1_opy_=False):
    hostname = bstack11lll11l1_opy_(url)
    is_private = bstack11llll11ll_opy_(hostname)
    try:
        if is_private or bstack111l11lll1_opy_:
            file_path = bstack11ll11111l1_opy_(bstack11ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᜸"), bstack11ll_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨ᜹"), logger)
            if os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨ᜺")) and eval(
                    os.environ.get(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩ᜻"))):
                return
            if (bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᜼") in config and not config[bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ᜽")]):
                os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬ᜾")] = str(True)
                bstack11ll111111l_opy_ = {bstack11ll_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ᜿"): hostname}
                bstack11ll1111ll1_opy_(bstack11ll_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᝀ"), bstack11ll_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨᝁ"), bstack11ll111111l_opy_, logger)
    except Exception as e:
        pass
def bstack1lll1ll1ll_opy_(caps, bstack11ll1111l1l_opy_):
    if bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᝂ") in caps:
        caps[bstack11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᝃ")][bstack11ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬᝄ")] = True
        if bstack11ll1111l1l_opy_:
            caps[bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᝅ")][bstack11ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᝆ")] = bstack11ll1111l1l_opy_
    else:
        caps[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧᝇ")] = True
        if bstack11ll1111l1l_opy_:
            caps[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᝈ")] = bstack11ll1111l1l_opy_
def bstack11ll1111lll_opy_(bstack1lll1ll1_opy_):
    bstack11ll11111ll_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᝉ"), bstack11ll_opy_ (u"ࠬ࠭ᝊ"))
    if bstack11ll11111ll_opy_ == bstack11ll_opy_ (u"࠭ࠧᝋ") or bstack11ll11111ll_opy_ == bstack11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᝌ"):
        threading.current_thread().testStatus = bstack1lll1ll1_opy_
    else:
        if bstack1lll1ll1_opy_ == bstack11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᝍ"):
            threading.current_thread().testStatus = bstack1lll1ll1_opy_