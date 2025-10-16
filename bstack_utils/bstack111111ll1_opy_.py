# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll11l111l_opy_, bstack1ll1l1l1ll_opy_, bstack1lll1l11_opy_, bstack1l11ll111l_opy_, \
    bstack11ll11l11l1_opy_
from bstack_utils.measure import measure
def bstack1ll1lll11l_opy_(bstack11ll11l1111_opy_):
    for driver in bstack11ll11l1111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack111l1l1lll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
def bstack1l1l1llll_opy_(driver, status, reason=bstack1lllll1_opy_ (u"ࠬ࠭ᛶ")):
    bstack11l1111l_opy_ = Config.bstack11111l1l_opy_()
    if bstack11l1111l_opy_.bstack111111l1_opy_():
        return
    bstack111111l11_opy_ = bstack111ll1111l_opy_(bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᛷ"), bstack1lllll1_opy_ (u"ࠧࠨᛸ"), status, reason, bstack1lllll1_opy_ (u"ࠨࠩ᛹"), bstack1lllll1_opy_ (u"ࠩࠪ᛺"))
    driver.execute_script(bstack111111l11_opy_)
@measure(event_name=EVENTS.bstack111l1l1lll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
def bstack11lllll11_opy_(page, status, reason=bstack1lllll1_opy_ (u"ࠪࠫ᛻")):
    try:
        if page is None:
            return
        bstack11l1111l_opy_ = Config.bstack11111l1l_opy_()
        if bstack11l1111l_opy_.bstack111111l1_opy_():
            return
        bstack111111l11_opy_ = bstack111ll1111l_opy_(bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ᛼"), bstack1lllll1_opy_ (u"ࠬ࠭᛽"), status, reason, bstack1lllll1_opy_ (u"࠭ࠧ᛾"), bstack1lllll1_opy_ (u"ࠧࠨ᛿"))
        page.evaluate(bstack1lllll1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᜀ"), bstack111111l11_opy_)
    except Exception as e:
        print(bstack1lllll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࢀࢃࠢᜁ"), e)
def bstack111ll1111l_opy_(type, name, status, reason, bstack1ll11lll11_opy_, bstack1l1ll1ll1l_opy_):
    bstack11111ll11l_opy_ = {
        bstack1lllll1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪᜂ"): type,
        bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜃ"): {}
    }
    if type == bstack1lllll1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧᜄ"):
        bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜅ")][bstack1lllll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᜆ")] = bstack1ll11lll11_opy_
        bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜇ")][bstack1lllll1_opy_ (u"ࠩࡧࡥࡹࡧࠧᜈ")] = json.dumps(str(bstack1l1ll1ll1l_opy_))
    if type == bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᜉ"):
        bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜊ")][bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᜋ")] = name
    if type == bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᜌ"):
        bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜍ")][bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜎ")] = status
        if status == bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᜏ") and str(reason) != bstack1lllll1_opy_ (u"ࠥࠦᜐ"):
            bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᜑ")][bstack1lllll1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᜒ")] = json.dumps(str(reason))
    bstack111l11ll1l_opy_ = bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᜓ").format(json.dumps(bstack11111ll11l_opy_))
    return bstack111l11ll1l_opy_
def bstack11ll1111ll_opy_(url, config, logger, bstack111lll1l1l_opy_=False):
    hostname = bstack1ll1l1l1ll_opy_(url)
    is_private = bstack1l11ll111l_opy_(hostname)
    try:
        if is_private or bstack111lll1l1l_opy_:
            file_path = bstack11ll11l111l_opy_(bstack1lllll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ᜔ࠧ"), bstack1lllll1_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴ᜕ࠧ"), logger)
            if os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ᜖")) and eval(
                    os.environ.get(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨ᜗"))):
                return
            if (bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᜘") in config and not config[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᜙")]):
                os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫ᜚")] = str(True)
                bstack11ll11l11ll_opy_ = {bstack1lllll1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ᜛"): hostname}
                bstack11ll11l11l1_opy_(bstack1lllll1_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧ᜜"), bstack1lllll1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ᜝"), bstack11ll11l11ll_opy_, logger)
    except Exception as e:
        pass
def bstack1l1ll1l111_opy_(caps, bstack11ll111llll_opy_):
    if bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ᜞") in caps:
        caps[bstack1lllll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᜟ")][bstack1lllll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫᜠ")] = True
        if bstack11ll111llll_opy_:
            caps[bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᜡ")][bstack1lllll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᜢ")] = bstack11ll111llll_opy_
    else:
        caps[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭ᜣ")] = True
        if bstack11ll111llll_opy_:
            caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᜤ")] = bstack11ll111llll_opy_
def bstack11ll111lll1_opy_(bstack1l1llll1_opy_):
    bstack11ll111ll1l_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧᜥ"), bstack1lllll1_opy_ (u"ࠫࠬᜦ"))
    if bstack11ll111ll1l_opy_ == bstack1lllll1_opy_ (u"ࠬ࠭ᜧ") or bstack11ll111ll1l_opy_ == bstack1lllll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᜨ"):
        threading.current_thread().testStatus = bstack1l1llll1_opy_
    else:
        if bstack1l1llll1_opy_ == bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᜩ"):
            threading.current_thread().testStatus = bstack1l1llll1_opy_