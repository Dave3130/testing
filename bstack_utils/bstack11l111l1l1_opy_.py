# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll11l1111_opy_, bstack1l11lll11l_opy_, bstack1ll1ll11_opy_, bstack1lll111l11_opy_, \
    bstack11ll111llll_opy_
from bstack_utils.measure import measure
def bstack1l1111lll_opy_(bstack11ll11l111l_opy_):
    for driver in bstack11ll11l111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1llll111l1_opy_, stage=STAGE.bstack1111l1111_opy_)
def bstack11l11lll1l_opy_(driver, status, reason=bstack1ll11_opy_ (u"ࠫࠬᛵ")):
    bstack1111ll11_opy_ = Config.bstack1llll11l1_opy_()
    if bstack1111ll11_opy_.bstack1111l11l_opy_():
        return
    bstack1lll11l11_opy_ = bstack11ll111ll1_opy_(bstack1ll11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᛶ"), bstack1ll11_opy_ (u"࠭ࠧᛷ"), status, reason, bstack1ll11_opy_ (u"ࠧࠨᛸ"), bstack1ll11_opy_ (u"ࠨࠩ᛹"))
    driver.execute_script(bstack1lll11l11_opy_)
@measure(event_name=EVENTS.bstack1llll111l1_opy_, stage=STAGE.bstack1111l1111_opy_)
def bstack1ll11l1l1_opy_(page, status, reason=bstack1ll11_opy_ (u"ࠩࠪ᛺")):
    try:
        if page is None:
            return
        bstack1111ll11_opy_ = Config.bstack1llll11l1_opy_()
        if bstack1111ll11_opy_.bstack1111l11l_opy_():
            return
        bstack1lll11l11_opy_ = bstack11ll111ll1_opy_(bstack1ll11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᛻"), bstack1ll11_opy_ (u"ࠫࠬ᛼"), status, reason, bstack1ll11_opy_ (u"ࠬ࠭᛽"), bstack1ll11_opy_ (u"࠭ࠧ᛾"))
        page.evaluate(bstack1ll11_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ᛿"), bstack1lll11l11_opy_)
    except Exception as e:
        print(bstack1ll11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨᜀ"), e)
def bstack11ll111ll1_opy_(type, name, status, reason, bstack1l1lll111l_opy_, bstack11llll1lll_opy_):
    bstack1l111l1111_opy_ = {
        bstack1ll11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩᜁ"): type,
        bstack1ll11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜂ"): {}
    }
    if type == bstack1ll11_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᜃ"):
        bstack1l111l1111_opy_[bstack1ll11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᜄ")][bstack1ll11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᜅ")] = bstack1l1lll111l_opy_
        bstack1l111l1111_opy_[bstack1ll11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᜆ")][bstack1ll11_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᜇ")] = json.dumps(str(bstack11llll1lll_opy_))
    if type == bstack1ll11_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᜈ"):
        bstack1l111l1111_opy_[bstack1ll11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜉ")][bstack1ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᜊ")] = name
    if type == bstack1ll11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᜋ"):
        bstack1l111l1111_opy_[bstack1ll11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜌ")][bstack1ll11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᜍ")] = status
        if status == bstack1ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᜎ") and str(reason) != bstack1ll11_opy_ (u"ࠤࠥᜏ"):
            bstack1l111l1111_opy_[bstack1ll11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜐ")][bstack1ll11_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᜑ")] = json.dumps(str(reason))
    bstack1l111lll11_opy_ = bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᜒ").format(json.dumps(bstack1l111l1111_opy_))
    return bstack1l111lll11_opy_
def bstack1ll1ll1lll_opy_(url, config, logger, bstack111l1l111l_opy_=False):
    hostname = bstack1l11lll11l_opy_(url)
    is_private = bstack1lll111l11_opy_(hostname)
    try:
        if is_private or bstack111l1l111l_opy_:
            file_path = bstack11ll11l1111_opy_(bstack1ll11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᜓ"), bstack1ll11_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ᜔࠭"), logger)
            if os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ᜕࠭")) and eval(
                    os.environ.get(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ᜖"))):
                return
            if (bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ᜗") in config and not config[bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᜘")]):
                os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ᜙")] = str(True)
                bstack11ll11l11l1_opy_ = {bstack1ll11_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ᜚"): hostname}
                bstack11ll111llll_opy_(bstack1ll11_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᜛"), bstack1ll11_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭᜜"), bstack11ll11l11l1_opy_, logger)
    except Exception as e:
        pass
def bstack1111l11lll_opy_(caps, bstack11ll11l11ll_opy_):
    if bstack1ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ᜝") in caps:
        caps[bstack1ll11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ᜞")][bstack1ll11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᜟ")] = True
        if bstack11ll11l11ll_opy_:
            caps[bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᜠ")][bstack1ll11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᜡ")] = bstack11ll11l11ll_opy_
    else:
        caps[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᜢ")] = True
        if bstack11ll11l11ll_opy_:
            caps[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᜣ")] = bstack11ll11l11ll_opy_
def bstack11ll111lll1_opy_(bstack11llllll_opy_):
    bstack11ll111ll1l_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᜤ"), bstack1ll11_opy_ (u"ࠪࠫᜥ"))
    if bstack11ll111ll1l_opy_ == bstack1ll11_opy_ (u"ࠫࠬᜦ") or bstack11ll111ll1l_opy_ == bstack1ll11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᜧ"):
        threading.current_thread().testStatus = bstack11llllll_opy_
    else:
        if bstack11llllll_opy_ == bstack1ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᜨ"):
            threading.current_thread().testStatus = bstack11llllll_opy_