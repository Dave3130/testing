# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1111ll1_opy_, bstack111lll1l1_opy_, bstack1l11l1l1_opy_, bstack11l11l1l11_opy_, \
    bstack11ll1111lll_opy_
from bstack_utils.measure import measure
def bstack11l11111l_opy_(bstack11ll1111l1l_opy_):
    for driver in bstack11ll1111l1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l11lllll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
def bstack1l1ll1l11_opy_(driver, status, reason=bstack1lllll1l_opy_ (u"ࠩࠪ᜖")):
    bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
    if bstack1lll1ll1l_opy_.bstack111ll111_opy_():
        return
    bstack111l1l1lll_opy_ = bstack111lll1l11_opy_(bstack1lllll1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᜗"), bstack1lllll1l_opy_ (u"ࠫࠬ᜘"), status, reason, bstack1lllll1l_opy_ (u"ࠬ࠭᜙"), bstack1lllll1l_opy_ (u"࠭ࠧ᜚"))
    driver.execute_script(bstack111l1l1lll_opy_)
@measure(event_name=EVENTS.bstack1l11lllll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
def bstack1l1ll111ll_opy_(page, status, reason=bstack1lllll1l_opy_ (u"ࠧࠨ᜛")):
    try:
        if page is None:
            return
        bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
        if bstack1lll1ll1l_opy_.bstack111ll111_opy_():
            return
        bstack111l1l1lll_opy_ = bstack111lll1l11_opy_(bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ᜜"), bstack1lllll1l_opy_ (u"ࠩࠪ᜝"), status, reason, bstack1lllll1l_opy_ (u"ࠪࠫ᜞"), bstack1lllll1l_opy_ (u"ࠫࠬᜟ"))
        page.evaluate(bstack1lllll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᜠ"), bstack111l1l1lll_opy_)
    except Exception as e:
        print(bstack1lllll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡽࢀࠦᜡ"), e)
def bstack111lll1l11_opy_(type, name, status, reason, bstack1l1l1ll1ll_opy_, bstack1111ll11l1_opy_):
    bstack11ll11111_opy_ = {
        bstack1lllll1l_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧᜢ"): type,
        bstack1lllll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜣ"): {}
    }
    if type == bstack1lllll1l_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫᜤ"):
        bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜥ")][bstack1lllll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᜦ")] = bstack1l1l1ll1ll_opy_
        bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜧ")][bstack1lllll1l_opy_ (u"࠭ࡤࡢࡶࡤࠫᜨ")] = json.dumps(str(bstack1111ll11l1_opy_))
    if type == bstack1lllll1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᜩ"):
        bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜪ")][bstack1lllll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᜫ")] = name
    if type == bstack1lllll1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᜬ"):
        bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜭ")][bstack1lllll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᜮ")] = status
        if status == bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᜯ") and str(reason) != bstack1lllll1l_opy_ (u"ࠢࠣᜰ"):
            bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜱ")][bstack1lllll1l_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᜲ")] = json.dumps(str(reason))
    bstack1l1l11ll11_opy_ = bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᜳ").format(json.dumps(bstack11ll11111_opy_))
    return bstack1l1l11ll11_opy_
def bstack1l11l1111_opy_(url, config, logger, bstack1ll1l1llll_opy_=False):
    hostname = bstack111lll1l1_opy_(url)
    is_private = bstack11l11l1l11_opy_(hostname)
    try:
        if is_private or bstack1ll1l1llll_opy_:
            file_path = bstack11ll1111ll1_opy_(bstack1lllll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮᜴ࠫ"), bstack1lllll1l_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫ᜵"), logger)
            if os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫ᜶")) and eval(
                    os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬ᜷"))):
                return
            if (bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ᜸") in config and not config[bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭᜹")]):
                os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨ᜺")] = str(True)
                bstack11ll111l111_opy_ = {bstack1lllll1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭᜻"): hostname}
                bstack11ll1111lll_opy_(bstack1lllll1l_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫ᜼"), bstack1lllll1l_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ᜽"), bstack11ll111l111_opy_, logger)
    except Exception as e:
        pass
def bstack1llll1l1l1_opy_(caps, bstack11ll11111ll_opy_):
    if bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ᜾") in caps:
        caps[bstack1lllll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ᜿")][bstack1lllll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨᝀ")] = True
        if bstack11ll11111ll_opy_:
            caps[bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᝁ")][bstack1lllll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᝂ")] = bstack11ll11111ll_opy_
    else:
        caps[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪᝃ")] = True
        if bstack11ll11111ll_opy_:
            caps[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᝄ")] = bstack11ll11111ll_opy_
def bstack11ll11111l1_opy_(bstack1l1lllll_opy_):
    bstack11ll1111l11_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫᝅ"), bstack1lllll1l_opy_ (u"ࠨࠩᝆ"))
    if bstack11ll1111l11_opy_ == bstack1lllll1l_opy_ (u"ࠩࠪᝇ") or bstack11ll1111l11_opy_ == bstack1lllll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᝈ"):
        threading.current_thread().testStatus = bstack1l1lllll_opy_
    else:
        if bstack1l1lllll_opy_ == bstack1lllll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᝉ"):
            threading.current_thread().testStatus = bstack1l1lllll_opy_