# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1111l1l_opy_, bstack1l1l1ll1l1_opy_, bstack1l11l1ll_opy_, bstack111lll111_opy_, \
    bstack11ll1111111_opy_
from bstack_utils.measure import measure
def bstack1111l1111l_opy_(bstack11ll11111l1_opy_):
    for driver in bstack11ll11111l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11lll1ll1_opy_, stage=STAGE.bstack1ll1ll111_opy_)
def bstack11ll1111l1_opy_(driver, status, reason=bstack111l1l_opy_ (u"࠭ࠧᜓ")):
    bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
    if bstack1lllll1l1_opy_.bstack1llll1ll1_opy_():
        return
    bstack111lll1ll_opy_ = bstack1ll1l1l1ll_opy_(bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵ᜔ࠪ"), bstack111l1l_opy_ (u"ࠨ᜕ࠩ"), status, reason, bstack111l1l_opy_ (u"ࠩࠪ᜖"), bstack111l1l_opy_ (u"ࠪࠫ᜗"))
    driver.execute_script(bstack111lll1ll_opy_)
@measure(event_name=EVENTS.bstack11lll1ll1_opy_, stage=STAGE.bstack1ll1ll111_opy_)
def bstack1lll11lll1_opy_(page, status, reason=bstack111l1l_opy_ (u"ࠫࠬ᜘")):
    try:
        if page is None:
            return
        bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
        if bstack1lllll1l1_opy_.bstack1llll1ll1_opy_():
            return
        bstack111lll1ll_opy_ = bstack1ll1l1l1ll_opy_(bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ᜙"), bstack111l1l_opy_ (u"࠭ࠧ᜚"), status, reason, bstack111l1l_opy_ (u"ࠧࠨ᜛"), bstack111l1l_opy_ (u"ࠨࠩ᜜"))
        page.evaluate(bstack111l1l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ᜝"), bstack111lll1ll_opy_)
    except Exception as e:
        print(bstack111l1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࢁࡽࠣ᜞"), e)
def bstack1ll1l1l1ll_opy_(type, name, status, reason, bstack1l11lll11_opy_, bstack1l11lllll_opy_):
    bstack11llllll1l_opy_ = {
        bstack111l1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫᜟ"): type,
        bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜠ"): {}
    }
    if type == bstack111l1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨᜡ"):
        bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜢ")][bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᜣ")] = bstack1l11lll11_opy_
        bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜤ")][bstack111l1l_opy_ (u"ࠪࡨࡦࡺࡡࠨᜥ")] = json.dumps(str(bstack1l11lllll_opy_))
    if type == bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᜦ"):
        bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜧ")][bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᜨ")] = name
    if type == bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᜩ"):
        bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜪ")][bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜫ")] = status
        if status == bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᜬ") and str(reason) != bstack111l1l_opy_ (u"ࠦࠧᜭ"):
            bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜮ")][bstack111l1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᜯ")] = json.dumps(str(reason))
    bstack1l1l1l1111_opy_ = bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬᜰ").format(json.dumps(bstack11llllll1l_opy_))
    return bstack1l1l1l1111_opy_
def bstack1l1l1lll1l_opy_(url, config, logger, bstack1111l1l1l1_opy_=False):
    hostname = bstack1l1l1ll1l1_opy_(url)
    is_private = bstack111lll111_opy_(hostname)
    try:
        if is_private or bstack1111l1l1l1_opy_:
            file_path = bstack11ll1111l1l_opy_(bstack111l1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᜱ"), bstack111l1l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᜲ"), logger)
            if os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜳ")) and eval(
                    os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓ᜴ࠩ"))):
                return
            if (bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᜵") in config and not config[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ᜶")]):
                os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬ᜷")] = str(True)
                bstack11ll1111l11_opy_ = {bstack111l1l_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ᜸"): hostname}
                bstack11ll1111111_opy_(bstack111l1l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨ᜹"), bstack111l1l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨ᜺"), bstack11ll1111l11_opy_, logger)
    except Exception as e:
        pass
def bstack1ll1l11ll_opy_(caps, bstack11ll111111l_opy_):
    if bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᜻") in caps:
        caps[bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᜼")][bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ᜽")] = True
        if bstack11ll111111l_opy_:
            caps[bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᜾")][bstack111l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ᜿")] = bstack11ll111111l_opy_
    else:
        caps[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧᝀ")] = True
        if bstack11ll111111l_opy_:
            caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᝁ")] = bstack11ll111111l_opy_
def bstack11ll11111ll_opy_(bstack1llll1ll_opy_):
    bstack11ll1111ll1_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᝂ"), bstack111l1l_opy_ (u"ࠬ࠭ᝃ"))
    if bstack11ll1111ll1_opy_ == bstack111l1l_opy_ (u"࠭ࠧᝄ") or bstack11ll1111ll1_opy_ == bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᝅ"):
        threading.current_thread().testStatus = bstack1llll1ll_opy_
    else:
        if bstack1llll1ll_opy_ == bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᝆ"):
            threading.current_thread().testStatus = bstack1llll1ll_opy_