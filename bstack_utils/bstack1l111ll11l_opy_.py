# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1111l11_opy_, bstack1l1lll11l1_opy_, bstack1l111l1l_opy_, bstack1l1111111_opy_, \
    bstack11ll1111l1l_opy_
from bstack_utils.measure import measure
def bstack111111l1l1_opy_(bstack11ll11111l1_opy_):
    for driver in bstack11ll11111l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1111l1ll1l_opy_, stage=STAGE.bstack111llllll_opy_)
def bstack1l1111ll1_opy_(driver, status, reason=bstack11l1l11_opy_ (u"ࠬ࠭ᜒ")):
    bstack111ll1ll_opy_ = Config.bstack1llll1lll_opy_()
    if bstack111ll1ll_opy_.bstack111111ll_opy_():
        return
    bstack11lll1111_opy_ = bstack1llll1ll11_opy_(bstack11l1l11_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜓ"), bstack11l1l11_opy_ (u"ࠧࠨ᜔"), status, reason, bstack11l1l11_opy_ (u"ࠨ᜕ࠩ"), bstack11l1l11_opy_ (u"ࠩࠪ᜖"))
    driver.execute_script(bstack11lll1111_opy_)
@measure(event_name=EVENTS.bstack1111l1ll1l_opy_, stage=STAGE.bstack111llllll_opy_)
def bstack1l11l111ll_opy_(page, status, reason=bstack11l1l11_opy_ (u"ࠪࠫ᜗")):
    try:
        if page is None:
            return
        bstack111ll1ll_opy_ = Config.bstack1llll1lll_opy_()
        if bstack111ll1ll_opy_.bstack111111ll_opy_():
            return
        bstack11lll1111_opy_ = bstack1llll1ll11_opy_(bstack11l1l11_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ᜘"), bstack11l1l11_opy_ (u"ࠬ࠭᜙"), status, reason, bstack11l1l11_opy_ (u"࠭ࠧ᜚"), bstack11l1l11_opy_ (u"ࠧࠨ᜛"))
        page.evaluate(bstack11l1l11_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ᜜"), bstack11lll1111_opy_)
    except Exception as e:
        print(bstack11l1l11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࢀࢃࠢ᜝"), e)
def bstack1llll1ll11_opy_(type, name, status, reason, bstack1l1llll11l_opy_, bstack1l1l1l11l1_opy_):
    bstack11l1llll1_opy_ = {
        bstack11l1l11_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ᜞"): type,
        bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜟ"): {}
    }
    if type == bstack11l1l11_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧᜠ"):
        bstack11l1llll1_opy_[bstack11l1l11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜡ")][bstack11l1l11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᜢ")] = bstack1l1llll11l_opy_
        bstack11l1llll1_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜣ")][bstack11l1l11_opy_ (u"ࠩࡧࡥࡹࡧࠧᜤ")] = json.dumps(str(bstack1l1l1l11l1_opy_))
    if type == bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᜥ"):
        bstack11l1llll1_opy_[bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜦ")][bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᜧ")] = name
    if type == bstack11l1l11_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜨ"):
        bstack11l1llll1_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜩ")][bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜪ")] = status
        if status == bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᜫ") and str(reason) != bstack11l1l11_opy_ (u"ࠥࠦᜬ"):
            bstack11l1llll1_opy_[bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜭ")][bstack11l1l11_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᜮ")] = json.dumps(str(reason))
    bstack11l1l11lll_opy_ = bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᜯ").format(json.dumps(bstack11l1llll1_opy_))
    return bstack11l1l11lll_opy_
def bstack11111l1ll1_opy_(url, config, logger, bstack111ll111l1_opy_=False):
    hostname = bstack1l1lll11l1_opy_(url)
    is_private = bstack1l1111111_opy_(hostname)
    try:
        if is_private or bstack111ll111l1_opy_:
            file_path = bstack11ll1111l11_opy_(bstack11l1l11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᜰ"), bstack11l1l11_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧᜱ"), logger)
            if os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᜲ")) and eval(
                    os.environ.get(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜳ"))):
                return
            if (bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᜴") in config and not config[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᜵")]):
                os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫ᜶")] = str(True)
                bstack11ll1111111_opy_ = {bstack11l1l11_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ᜷"): hostname}
                bstack11ll1111l1l_opy_(bstack11l1l11_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧ᜸"), bstack11l1l11_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ᜹"), bstack11ll1111111_opy_, logger)
    except Exception as e:
        pass
def bstack11l1ll1lll_opy_(caps, bstack11ll1111ll1_opy_):
    if bstack11l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ᜺") in caps:
        caps[bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᜻")][bstack11l1l11_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫ᜼")] = True
        if bstack11ll1111ll1_opy_:
            caps[bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᜽")][bstack11l1l11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ᜾")] = bstack11ll1111ll1_opy_
    else:
        caps[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭᜿")] = True
        if bstack11ll1111ll1_opy_:
            caps[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᝀ")] = bstack11ll1111ll1_opy_
def bstack11ll111111l_opy_(bstack1lll1ll1_opy_):
    bstack11ll11111ll_opy_ = bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧᝁ"), bstack11l1l11_opy_ (u"ࠫࠬᝂ"))
    if bstack11ll11111ll_opy_ == bstack11l1l11_opy_ (u"ࠬ࠭ᝃ") or bstack11ll11111ll_opy_ == bstack11l1l11_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᝄ"):
        threading.current_thread().testStatus = bstack1lll1ll1_opy_
    else:
        if bstack1lll1ll1_opy_ == bstack11l1l11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᝅ"):
            threading.current_thread().testStatus = bstack1lll1ll1_opy_