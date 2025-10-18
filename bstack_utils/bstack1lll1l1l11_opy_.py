# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1111l1l_opy_, bstack1ll1llllll_opy_, bstack1l1lll11_opy_, bstack11ll1ll111_opy_, \
    bstack11ll1111ll1_opy_
from bstack_utils.measure import measure
def bstack11lllll11l_opy_(bstack11ll1111lll_opy_):
    for driver in bstack11ll1111lll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll11l11l_opy_, stage=STAGE.bstack1l11lll11_opy_)
def bstack11ll11lll1_opy_(driver, status, reason=bstack11l111_opy_ (u"ࠫࠬ᜘")):
    bstack11111l11_opy_ = Config.bstack111l11l1_opy_()
    if bstack11111l11_opy_.bstack111l1l1l_opy_():
        return
    bstack1l111l1l1l_opy_ = bstack1ll1lll11l_opy_(bstack11l111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ᜙"), bstack11l111_opy_ (u"࠭ࠧ᜚"), status, reason, bstack11l111_opy_ (u"ࠧࠨ᜛"), bstack11l111_opy_ (u"ࠨࠩ᜜"))
    driver.execute_script(bstack1l111l1l1l_opy_)
@measure(event_name=EVENTS.bstack1ll11l11l_opy_, stage=STAGE.bstack1l11lll11_opy_)
def bstack1lll111lll_opy_(page, status, reason=bstack11l111_opy_ (u"ࠩࠪ᜝")):
    try:
        if page is None:
            return
        bstack11111l11_opy_ = Config.bstack111l11l1_opy_()
        if bstack11111l11_opy_.bstack111l1l1l_opy_():
            return
        bstack1l111l1l1l_opy_ = bstack1ll1lll11l_opy_(bstack11l111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᜞"), bstack11l111_opy_ (u"ࠫࠬᜟ"), status, reason, bstack11l111_opy_ (u"ࠬ࠭ᜠ"), bstack11l111_opy_ (u"࠭ࠧᜡ"))
        page.evaluate(bstack11l111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᜢ"), bstack1l111l1l1l_opy_)
    except Exception as e:
        print(bstack11l111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨᜣ"), e)
def bstack1ll1lll11l_opy_(type, name, status, reason, bstack11lll1l11_opy_, bstack1111l11l1l_opy_):
    bstack1ll1111111_opy_ = {
        bstack11l111_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩᜤ"): type,
        bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜥ"): {}
    }
    if type == bstack11l111_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᜦ"):
        bstack1ll1111111_opy_[bstack11l111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜧ")][bstack11l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᜨ")] = bstack11lll1l11_opy_
        bstack1ll1111111_opy_[bstack11l111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜩ")][bstack11l111_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᜪ")] = json.dumps(str(bstack1111l11l1l_opy_))
    if type == bstack11l111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᜫ"):
        bstack1ll1111111_opy_[bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜬ")][bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᜭ")] = name
    if type == bstack11l111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᜮ"):
        bstack1ll1111111_opy_[bstack11l111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜯ")][bstack11l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᜰ")] = status
        if status == bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᜱ") and str(reason) != bstack11l111_opy_ (u"ࠤࠥᜲ"):
            bstack1ll1111111_opy_[bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜳ")][bstack11l111_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱ᜴ࠫ")] = json.dumps(str(reason))
    bstack1l1l1l1111_opy_ = bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ᜵").format(json.dumps(bstack1ll1111111_opy_))
    return bstack1l1l1l1111_opy_
def bstack1ll1ll1l1l_opy_(url, config, logger, bstack1ll111llll_opy_=False):
    hostname = bstack1ll1llllll_opy_(url)
    is_private = bstack11ll1ll111_opy_(hostname)
    try:
        if is_private or bstack1ll111llll_opy_:
            file_path = bstack11ll1111l1l_opy_(bstack11l111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭᜶"), bstack11l111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᜷"), logger)
            if os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭᜸")) and eval(
                    os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ᜹"))):
                return
            if (bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ᜺") in config and not config[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᜻")]):
                os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ᜼")] = str(True)
                bstack11ll11111l1_opy_ = {bstack11l111_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ᜽"): hostname}
                bstack11ll1111ll1_opy_(bstack11l111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᜾"), bstack11l111_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭᜿"), bstack11ll11111l1_opy_, logger)
    except Exception as e:
        pass
def bstack11lll1llll_opy_(caps, bstack11ll1111l11_opy_):
    if bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᝀ") in caps:
        caps[bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᝁ")][bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᝂ")] = True
        if bstack11ll1111l11_opy_:
            caps[bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᝃ")][bstack11l111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᝄ")] = bstack11ll1111l11_opy_
    else:
        caps[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᝅ")] = True
        if bstack11ll1111l11_opy_:
            caps[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᝆ")] = bstack11ll1111l11_opy_
def bstack11ll11111ll_opy_(bstack1llll111_opy_):
    bstack11ll111l111_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᝇ"), bstack11l111_opy_ (u"ࠪࠫᝈ"))
    if bstack11ll111l111_opy_ == bstack11l111_opy_ (u"ࠫࠬᝉ") or bstack11ll111l111_opy_ == bstack11l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᝊ"):
        threading.current_thread().testStatus = bstack1llll111_opy_
    else:
        if bstack1llll111_opy_ == bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᝋ"):
            threading.current_thread().testStatus = bstack1llll111_opy_