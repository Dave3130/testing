# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll111111l_opy_, bstack1lll1l1111_opy_, bstack1lll111l_opy_, bstack11l11111ll_opy_, \
    bstack11ll1111l1l_opy_
from bstack_utils.measure import measure
def bstack11l11lll1_opy_(bstack11ll11111ll_opy_):
    for driver in bstack11ll11111ll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11l1111lll_opy_, stage=STAGE.bstack11ll1ll11_opy_)
def bstack1lllll1l1l_opy_(driver, status, reason=bstack11lll1_opy_ (u"ࠬ࠭ᜒ")):
    bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
    if bstack1lll1l11l_opy_.bstack111ll111_opy_():
        return
    bstack1llll111l1_opy_ = bstack11l111111l_opy_(bstack11lll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜓ"), bstack11lll1_opy_ (u"ࠧࠨ᜔"), status, reason, bstack11lll1_opy_ (u"ࠨ᜕ࠩ"), bstack11lll1_opy_ (u"ࠩࠪ᜖"))
    driver.execute_script(bstack1llll111l1_opy_)
@measure(event_name=EVENTS.bstack11l1111lll_opy_, stage=STAGE.bstack11ll1ll11_opy_)
def bstack1l1lll111l_opy_(page, status, reason=bstack11lll1_opy_ (u"ࠪࠫ᜗")):
    try:
        if page is None:
            return
        bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
        if bstack1lll1l11l_opy_.bstack111ll111_opy_():
            return
        bstack1llll111l1_opy_ = bstack11l111111l_opy_(bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ᜘"), bstack11lll1_opy_ (u"ࠬ࠭᜙"), status, reason, bstack11lll1_opy_ (u"࠭ࠧ᜚"), bstack11lll1_opy_ (u"ࠧࠨ᜛"))
        page.evaluate(bstack11lll1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ᜜"), bstack1llll111l1_opy_)
    except Exception as e:
        print(bstack11lll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࢀࢃࠢ᜝"), e)
def bstack11l111111l_opy_(type, name, status, reason, bstack11l1lll1l_opy_, bstack11ll1l1111_opy_):
    bstack1111l1l111_opy_ = {
        bstack11lll1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ᜞"): type,
        bstack11lll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜟ"): {}
    }
    if type == bstack11lll1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧᜠ"):
        bstack1111l1l111_opy_[bstack11lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜡ")][bstack11lll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᜢ")] = bstack11l1lll1l_opy_
        bstack1111l1l111_opy_[bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜣ")][bstack11lll1_opy_ (u"ࠩࡧࡥࡹࡧࠧᜤ")] = json.dumps(str(bstack11ll1l1111_opy_))
    if type == bstack11lll1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᜥ"):
        bstack1111l1l111_opy_[bstack11lll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜦ")][bstack11lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᜧ")] = name
    if type == bstack11lll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜨ"):
        bstack1111l1l111_opy_[bstack11lll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜩ")][bstack11lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜪ")] = status
        if status == bstack11lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᜫ") and str(reason) != bstack11lll1_opy_ (u"ࠥࠦᜬ"):
            bstack1111l1l111_opy_[bstack11lll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜭ")][bstack11lll1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᜮ")] = json.dumps(str(reason))
    bstack111llll1ll_opy_ = bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᜯ").format(json.dumps(bstack1111l1l111_opy_))
    return bstack111llll1ll_opy_
def bstack111l1l1lll_opy_(url, config, logger, bstack11llllll11_opy_=False):
    hostname = bstack1lll1l1111_opy_(url)
    is_private = bstack11l11111ll_opy_(hostname)
    try:
        if is_private or bstack11llllll11_opy_:
            file_path = bstack11ll111111l_opy_(bstack11lll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᜰ"), bstack11lll1_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᜱ"), logger)
            if os.environ.get(bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᜲ")) and eval(
                    os.environ.get(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜳ"))):
                return
            if (bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᜴") in config and not config[bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᜵")]):
                os.environ[bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫ᜶")] = str(True)
                bstack11ll11111l1_opy_ = {bstack11lll1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ᜷"): hostname}
                bstack11ll1111l1l_opy_(bstack11lll1_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧ᜸"), bstack11lll1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ᜹"), bstack11ll11111l1_opy_, logger)
    except Exception as e:
        pass
def bstack11l11111l_opy_(caps, bstack11ll1111ll1_opy_):
    if bstack11lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ᜺") in caps:
        caps[bstack11lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᜻")][bstack11lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫ᜼")] = True
        if bstack11ll1111ll1_opy_:
            caps[bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᜽")][bstack11lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᜾")] = bstack11ll1111ll1_opy_
    else:
        caps[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭᜿")] = True
        if bstack11ll1111ll1_opy_:
            caps[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᝀ")] = bstack11ll1111ll1_opy_
def bstack11ll1111l11_opy_(bstack1llll1ll_opy_):
    bstack11ll1111lll_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧᝁ"), bstack11lll1_opy_ (u"ࠫࠬᝂ"))
    if bstack11ll1111lll_opy_ == bstack11lll1_opy_ (u"ࠬ࠭ᝃ") or bstack11ll1111lll_opy_ == bstack11lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᝄ"):
        threading.current_thread().testStatus = bstack1llll1ll_opy_
    else:
        if bstack1llll1ll_opy_ == bstack11lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᝅ"):
            threading.current_thread().testStatus = bstack1llll1ll_opy_