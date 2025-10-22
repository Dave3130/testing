# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1111ll1_opy_, bstack1l11ll1ll1_opy_, bstack1l1111ll_opy_, bstack1l11l1lll_opy_, \
    bstack11ll111111l_opy_
from bstack_utils.measure import measure
def bstack11ll11111l_opy_(bstack11ll1111l11_opy_):
    for driver in bstack11ll1111l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll1111l11_opy_, stage=STAGE.bstack1ll11l111l_opy_)
def bstack11lllll11_opy_(driver, status, reason=bstack1l111ll_opy_ (u"࠭ࠧᜓ")):
    bstack111l11ll_opy_ = Config.bstack111l11l1_opy_()
    if bstack111l11ll_opy_.bstack111l1lll_opy_():
        return
    bstack1l11ll111_opy_ = bstack1l11lll11_opy_(bstack1l111ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵ᜔ࠪ"), bstack1l111ll_opy_ (u"ࠨ᜕ࠩ"), status, reason, bstack1l111ll_opy_ (u"ࠩࠪ᜖"), bstack1l111ll_opy_ (u"ࠪࠫ᜗"))
    driver.execute_script(bstack1l11ll111_opy_)
@measure(event_name=EVENTS.bstack1ll1111l11_opy_, stage=STAGE.bstack1ll11l111l_opy_)
def bstack11111lll1l_opy_(page, status, reason=bstack1l111ll_opy_ (u"ࠫࠬ᜘")):
    try:
        if page is None:
            return
        bstack111l11ll_opy_ = Config.bstack111l11l1_opy_()
        if bstack111l11ll_opy_.bstack111l1lll_opy_():
            return
        bstack1l11ll111_opy_ = bstack1l11lll11_opy_(bstack1l111ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ᜙"), bstack1l111ll_opy_ (u"࠭ࠧ᜚"), status, reason, bstack1l111ll_opy_ (u"ࠧࠨ᜛"), bstack1l111ll_opy_ (u"ࠨࠩ᜜"))
        page.evaluate(bstack1l111ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ᜝"), bstack1l11ll111_opy_)
    except Exception as e:
        print(bstack1l111ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࢁࡽࠣ᜞"), e)
def bstack1l11lll11_opy_(type, name, status, reason, bstack11llll111l_opy_, bstack111l11l11_opy_):
    bstack1l11ll111l_opy_ = {
        bstack1l111ll_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫᜟ"): type,
        bstack1l111ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜠ"): {}
    }
    if type == bstack1l111ll_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨᜡ"):
        bstack1l11ll111l_opy_[bstack1l111ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜢ")][bstack1l111ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᜣ")] = bstack11llll111l_opy_
        bstack1l11ll111l_opy_[bstack1l111ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜤ")][bstack1l111ll_opy_ (u"ࠪࡨࡦࡺࡡࠨᜥ")] = json.dumps(str(bstack111l11l11_opy_))
    if type == bstack1l111ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᜦ"):
        bstack1l11ll111l_opy_[bstack1l111ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜧ")][bstack1l111ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᜨ")] = name
    if type == bstack1l111ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪᜩ"):
        bstack1l11ll111l_opy_[bstack1l111ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜪ")][bstack1l111ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜫ")] = status
        if status == bstack1l111ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᜬ") and str(reason) != bstack1l111ll_opy_ (u"ࠦࠧᜭ"):
            bstack1l11ll111l_opy_[bstack1l111ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜮ")][bstack1l111ll_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ᜯ")] = json.dumps(str(reason))
    bstack1l11ll11l_opy_ = bstack1l111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬᜰ").format(json.dumps(bstack1l11ll111l_opy_))
    return bstack1l11ll11l_opy_
def bstack1l11lll111_opy_(url, config, logger, bstack1111llll1l_opy_=False):
    hostname = bstack1l11ll1ll1_opy_(url)
    is_private = bstack1l11l1lll_opy_(hostname)
    try:
        if is_private or bstack1111llll1l_opy_:
            file_path = bstack11ll1111ll1_opy_(bstack1l111ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᜱ"), bstack1l111ll_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨᜲ"), logger)
            if os.environ.get(bstack1l111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜳ")) and eval(
                    os.environ.get(bstack1l111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓ᜴ࠩ"))):
                return
            if (bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᜵") in config and not config[bstack1l111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ᜶")]):
                os.environ[bstack1l111ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬ᜷")] = str(True)
                bstack11ll11111l1_opy_ = {bstack1l111ll_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ᜸"): hostname}
                bstack11ll111111l_opy_(bstack1l111ll_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨ᜹"), bstack1l111ll_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨ᜺"), bstack11ll11111l1_opy_, logger)
    except Exception as e:
        pass
def bstack111llllll1_opy_(caps, bstack11ll1111111_opy_):
    if bstack1l111ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᜻") in caps:
        caps[bstack1l111ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᜼")][bstack1l111ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ᜽")] = True
        if bstack11ll1111111_opy_:
            caps[bstack1l111ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᜾")][bstack1l111ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ᜿")] = bstack11ll1111111_opy_
    else:
        caps[bstack1l111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧᝀ")] = True
        if bstack11ll1111111_opy_:
            caps[bstack1l111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᝁ")] = bstack11ll1111111_opy_
def bstack11ll11111ll_opy_(bstack11llll1l_opy_):
    bstack11ll1111l1l_opy_ = bstack1l1111ll_opy_(threading.current_thread(), bstack1l111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᝂ"), bstack1l111ll_opy_ (u"ࠬ࠭ᝃ"))
    if bstack11ll1111l1l_opy_ == bstack1l111ll_opy_ (u"࠭ࠧᝄ") or bstack11ll1111l1l_opy_ == bstack1l111ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᝅ"):
        threading.current_thread().testStatus = bstack11llll1l_opy_
    else:
        if bstack11llll1l_opy_ == bstack1l111ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᝆ"):
            threading.current_thread().testStatus = bstack11llll1l_opy_