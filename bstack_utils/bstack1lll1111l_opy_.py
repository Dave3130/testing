# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll111l1l1_opy_, bstack1lllll1l1l_opy_, bstack1l11lll1_opy_, bstack1111ll1l11_opy_, \
    bstack11ll111llll_opy_
from bstack_utils.measure import measure
def bstack1l111llll1_opy_(bstack11ll111l11l_opy_):
    for driver in bstack11ll111l11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack111l1llll_opy_, stage=STAGE.bstack1l111l11l_opy_)
def bstack1ll1ll1l11_opy_(driver, status, reason=bstack11l111_opy_ (u"ࠩࠪᛥ")):
    bstack111ll111_opy_ = Config.bstack111ll1ll_opy_()
    if bstack111ll111_opy_.bstack1lll1ll11_opy_():
        return
    bstack1111l1l11_opy_ = bstack1ll11l11ll_opy_(bstack11l111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᛦ"), bstack11l111_opy_ (u"ࠫࠬᛧ"), status, reason, bstack11l111_opy_ (u"ࠬ࠭ᛨ"), bstack11l111_opy_ (u"࠭ࠧᛩ"))
    driver.execute_script(bstack1111l1l11_opy_)
@measure(event_name=EVENTS.bstack111l1llll_opy_, stage=STAGE.bstack1l111l11l_opy_)
def bstack1l11l11ll_opy_(page, status, reason=bstack11l111_opy_ (u"ࠧࠨᛪ")):
    try:
        if page is None:
            return
        bstack111ll111_opy_ = Config.bstack111ll1ll_opy_()
        if bstack111ll111_opy_.bstack1lll1ll11_opy_():
            return
        bstack1111l1l11_opy_ = bstack1ll11l11ll_opy_(bstack11l111_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ᛫"), bstack11l111_opy_ (u"ࠩࠪ᛬"), status, reason, bstack11l111_opy_ (u"ࠪࠫ᛭"), bstack11l111_opy_ (u"ࠫࠬᛮ"))
        page.evaluate(bstack11l111_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᛯ"), bstack1111l1l11_opy_)
    except Exception as e:
        print(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡽࢀࠦᛰ"), e)
def bstack1ll11l11ll_opy_(type, name, status, reason, bstack1ll1l1l11_opy_, bstack1l11l1l1l1_opy_):
    bstack11l1ll111l_opy_ = {
        bstack11l111_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧᛱ"): type,
        bstack11l111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᛲ"): {}
    }
    if type == bstack11l111_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫᛳ"):
        bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᛴ")][bstack11l111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᛵ")] = bstack1ll1l1l11_opy_
        bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᛶ")][bstack11l111_opy_ (u"࠭ࡤࡢࡶࡤࠫᛷ")] = json.dumps(str(bstack1l11l1l1l1_opy_))
    if type == bstack11l111_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᛸ"):
        bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ᛹")][bstack11l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ᛺")] = name
    if type == bstack11l111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᛻"):
        bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ᛼")][bstack11l111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ᛽")] = status
        if status == bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᛾") and str(reason) != bstack11l111_opy_ (u"ࠢࠣ᛿"):
            bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜀ")][bstack11l111_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᜁ")] = json.dumps(str(reason))
    bstack1111l11ll1_opy_ = bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᜂ").format(json.dumps(bstack11l1ll111l_opy_))
    return bstack1111l11ll1_opy_
def bstack1l11111l1l_opy_(url, config, logger, bstack1lll11111_opy_=False):
    hostname = bstack1lllll1l1l_opy_(url)
    is_private = bstack1111ll1l11_opy_(hostname)
    try:
        if is_private or bstack1lll11111_opy_:
            file_path = bstack11ll111l1l1_opy_(bstack11l111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᜃ"), bstack11l111_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᜄ"), logger)
            if os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᜅ")) and eval(
                    os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᜆ"))):
                return
            if (bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᜇ") in config and not config[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᜈ")]):
                os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜉ")] = str(True)
                bstack11ll111l1ll_opy_ = {bstack11l111_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ᜊ"): hostname}
                bstack11ll111llll_opy_(bstack11l111_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᜋ"), bstack11l111_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫᜌ"), bstack11ll111l1ll_opy_, logger)
    except Exception as e:
        pass
def bstack1l1l1ll1ll_opy_(caps, bstack11ll111ll1l_opy_):
    if bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᜍ") in caps:
        caps[bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᜎ")][bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨᜏ")] = True
        if bstack11ll111ll1l_opy_:
            caps[bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᜐ")][bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᜑ")] = bstack11ll111ll1l_opy_
    else:
        caps[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪᜒ")] = True
        if bstack11ll111ll1l_opy_:
            caps[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᜓ")] = bstack11ll111ll1l_opy_
def bstack11ll111ll11_opy_(bstack1ll111l1_opy_):
    bstack11ll111lll1_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶ᜔ࠫ"), bstack11l111_opy_ (u"ࠨ᜕ࠩ"))
    if bstack11ll111lll1_opy_ == bstack11l111_opy_ (u"ࠩࠪ᜖") or bstack11ll111lll1_opy_ == bstack11l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᜗"):
        threading.current_thread().testStatus = bstack1ll111l1_opy_
    else:
        if bstack1ll111l1_opy_ == bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᜘"):
            threading.current_thread().testStatus = bstack1ll111l1_opy_