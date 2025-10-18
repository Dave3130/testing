# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll111l1ll_opy_, bstack1l111111l_opy_, bstack1l1l1l1l_opy_, bstack1l1lll1l11_opy_, \
    bstack11ll111lll1_opy_
from bstack_utils.measure import measure
def bstack1l11ll11l1_opy_(bstack11ll11l1111_opy_):
    for driver in bstack11ll11l1111_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack111llll1l_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack111lll1111_opy_(driver, status, reason=bstack1l1lll1_opy_ (u"ࠧࠨᛱ")):
    bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
    if bstack1111111l_opy_.bstack11111ll1_opy_():
        return
    bstack1lllll11ll_opy_ = bstack1l11llll1_opy_(bstack1l1lll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫᛲ"), bstack1l1lll1_opy_ (u"ࠩࠪᛳ"), status, reason, bstack1l1lll1_opy_ (u"ࠪࠫᛴ"), bstack1l1lll1_opy_ (u"ࠫࠬᛵ"))
    driver.execute_script(bstack1lllll11ll_opy_)
@measure(event_name=EVENTS.bstack111llll1l_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack1111l1ll11_opy_(page, status, reason=bstack1l1lll1_opy_ (u"ࠬ࠭ᛶ")):
    try:
        if page is None:
            return
        bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
        if bstack1111111l_opy_.bstack11111ll1_opy_():
            return
        bstack1lllll11ll_opy_ = bstack1l11llll1_opy_(bstack1l1lll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᛷ"), bstack1l1lll1_opy_ (u"ࠧࠨᛸ"), status, reason, bstack1l1lll1_opy_ (u"ࠨࠩ᛹"), bstack1l1lll1_opy_ (u"ࠩࠪ᛺"))
        page.evaluate(bstack1l1lll1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ᛻"), bstack1lllll11ll_opy_)
    except Exception as e:
        print(bstack1l1lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡻࡾࠤ᛼"), e)
def bstack1l11llll1_opy_(type, name, status, reason, bstack1ll1llll1l_opy_, bstack11111llll_opy_):
    bstack1ll11ll1l1_opy_ = {
        bstack1l1lll1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ᛽"): type,
        bstack1l1lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ᛾"): {}
    }
    if type == bstack1l1lll1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ᛿"):
        bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜀ")][bstack1l1lll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᜁ")] = bstack1ll1llll1l_opy_
        bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᜂ")][bstack1l1lll1_opy_ (u"ࠫࡩࡧࡴࡢࠩᜃ")] = json.dumps(str(bstack11111llll_opy_))
    if type == bstack1l1lll1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᜄ"):
        bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜅ")][bstack1l1lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᜆ")] = name
    if type == bstack1l1lll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫᜇ"):
        bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜈ")][bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᜉ")] = status
        if status == bstack1l1lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᜊ") and str(reason) != bstack1l1lll1_opy_ (u"ࠧࠨᜋ"):
            bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᜌ")][bstack1l1lll1_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧᜍ")] = json.dumps(str(reason))
    bstack1l1111111l_opy_ = bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ᜎ").format(json.dumps(bstack1ll11ll1l1_opy_))
    return bstack1l1111111l_opy_
def bstack11l1lll1l1_opy_(url, config, logger, bstack1ll1llll1_opy_=False):
    hostname = bstack1l111111l_opy_(url)
    is_private = bstack1l1lll1l11_opy_(hostname)
    try:
        if is_private or bstack1ll1llll1_opy_:
            file_path = bstack11ll111l1ll_opy_(bstack1l1lll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᜏ"), bstack1l1lll1_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩᜐ"), logger)
            if os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᜑ")) and eval(
                    os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᜒ"))):
                return
            if (bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪᜓ") in config and not config[bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯᜔ࠫ")]):
                os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ᜕࠭")] = str(True)
                bstack11ll111llll_opy_ = {bstack1l1lll1_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ᜖"): hostname}
                bstack11ll111lll1_opy_(bstack1l1lll1_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩ᜗"), bstack1l1lll1_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩ᜘"), bstack11ll111llll_opy_, logger)
    except Exception as e:
        pass
def bstack11llll1111_opy_(caps, bstack11ll111ll11_opy_):
    if bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᜙") in caps:
        caps[bstack1l1lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ᜚")][bstack1l1lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭᜛")] = True
        if bstack11ll111ll11_opy_:
            caps[bstack1l1lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ᜜")][bstack1l1lll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ᜝")] = bstack11ll111ll11_opy_
    else:
        caps[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨ᜞")] = True
        if bstack11ll111ll11_opy_:
            caps[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᜟ")] = bstack11ll111ll11_opy_
def bstack11ll111ll1l_opy_(bstack1ll1ll1l_opy_):
    bstack11ll111l1l1_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩᜠ"), bstack1l1lll1_opy_ (u"࠭ࠧᜡ"))
    if bstack11ll111l1l1_opy_ == bstack1l1lll1_opy_ (u"ࠧࠨᜢ") or bstack11ll111l1l1_opy_ == bstack1l1lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᜣ"):
        threading.current_thread().testStatus = bstack1ll1ll1l_opy_
    else:
        if bstack1ll1ll1l_opy_ == bstack1l1lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᜤ"):
            threading.current_thread().testStatus = bstack1ll1ll1l_opy_