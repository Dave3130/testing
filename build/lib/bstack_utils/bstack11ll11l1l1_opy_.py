# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll111l1ll_opy_, bstack1llll1llll_opy_, bstack1l1lllll_opy_, bstack111l11lll1_opy_, \
    bstack11ll111ll11_opy_
from bstack_utils.measure import measure
def bstack11l1ll1l11_opy_(bstack11ll111ll1l_opy_):
    for driver in bstack11ll111ll1l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11l1l111ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack1111ll1l11_opy_(driver, status, reason=bstack11111_opy_ (u"ࠩࠪᛥ")):
    bstack11l1111l_opy_ = Config.bstack111111ll_opy_()
    if bstack11l1111l_opy_.bstack1lll1lll1_opy_():
        return
    bstack1ll11l1l11_opy_ = bstack1lllll1l1l_opy_(bstack11111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᛦ"), bstack11111_opy_ (u"ࠫࠬᛧ"), status, reason, bstack11111_opy_ (u"ࠬ࠭ᛨ"), bstack11111_opy_ (u"࠭ࠧᛩ"))
    driver.execute_script(bstack1ll11l1l11_opy_)
@measure(event_name=EVENTS.bstack11l1l111ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack1ll1l11l1_opy_(page, status, reason=bstack11111_opy_ (u"ࠧࠨᛪ")):
    try:
        if page is None:
            return
        bstack11l1111l_opy_ = Config.bstack111111ll_opy_()
        if bstack11l1111l_opy_.bstack1lll1lll1_opy_():
            return
        bstack1ll11l1l11_opy_ = bstack1lllll1l1l_opy_(bstack11111_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ᛫"), bstack11111_opy_ (u"ࠩࠪ᛬"), status, reason, bstack11111_opy_ (u"ࠪࠫ᛭"), bstack11111_opy_ (u"ࠫࠬᛮ"))
        page.evaluate(bstack11111_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᛯ"), bstack1ll11l1l11_opy_)
    except Exception as e:
        print(bstack11111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡽࢀࠦᛰ"), e)
def bstack1lllll1l1l_opy_(type, name, status, reason, bstack111l1l1l11_opy_, bstack11l1l1111_opy_):
    bstack1ll1llllll_opy_ = {
        bstack11111_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧᛱ"): type,
        bstack11111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᛲ"): {}
    }
    if type == bstack11111_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫᛳ"):
        bstack1ll1llllll_opy_[bstack11111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᛴ")][bstack11111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᛵ")] = bstack111l1l1l11_opy_
        bstack1ll1llllll_opy_[bstack11111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᛶ")][bstack11111_opy_ (u"࠭ࡤࡢࡶࡤࠫᛷ")] = json.dumps(str(bstack11l1l1111_opy_))
    if type == bstack11111_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᛸ"):
        bstack1ll1llllll_opy_[bstack11111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ᛹")][bstack11111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ᛺")] = name
    if type == bstack11111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᛻"):
        bstack1ll1llllll_opy_[bstack11111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ᛼")][bstack11111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ᛽")] = status
        if status == bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᛾") and str(reason) != bstack11111_opy_ (u"ࠢࠣ᛿"):
            bstack1ll1llllll_opy_[bstack11111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᜀ")][bstack11111_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩᜁ")] = json.dumps(str(reason))
    bstack11llll111_opy_ = bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᜂ").format(json.dumps(bstack1ll1llllll_opy_))
    return bstack11llll111_opy_
def bstack1ll11l1l1l_opy_(url, config, logger, bstack1ll1lll1l_opy_=False):
    hostname = bstack1llll1llll_opy_(url)
    is_private = bstack111l11lll1_opy_(hostname)
    try:
        if is_private or bstack1ll1lll1l_opy_:
            file_path = bstack11ll111l1ll_opy_(bstack11111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫᜃ"), bstack11111_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᜄ"), logger)
            if os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫᜅ")) and eval(
                    os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᜆ"))):
                return
            if (bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᜇ") in config and not config[bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᜈ")]):
                os.environ[bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨᜉ")] = str(True)
                bstack11ll111lll1_opy_ = {bstack11111_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ᜊ"): hostname}
                bstack11ll111ll11_opy_(bstack11111_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫᜋ"), bstack11111_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫᜌ"), bstack11ll111lll1_opy_, logger)
    except Exception as e:
        pass
def bstack1lll1l1lll_opy_(caps, bstack11ll111llll_opy_):
    if bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᜍ") in caps:
        caps[bstack11111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᜎ")][bstack11111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨᜏ")] = True
        if bstack11ll111llll_opy_:
            caps[bstack11111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᜐ")][bstack11111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ᜑ")] = bstack11ll111llll_opy_
    else:
        caps[bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪᜒ")] = True
        if bstack11ll111llll_opy_:
            caps[bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᜓ")] = bstack11ll111llll_opy_
def bstack11ll11l1111_opy_(bstack1l1llll1_opy_):
    bstack11ll111l1l1_opy_ = bstack1l1lllll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶ᜔ࠫ"), bstack11111_opy_ (u"ࠨ᜕ࠩ"))
    if bstack11ll111l1l1_opy_ == bstack11111_opy_ (u"ࠩࠪ᜖") or bstack11ll111l1l1_opy_ == bstack11111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᜗"):
        threading.current_thread().testStatus = bstack1l1llll1_opy_
    else:
        if bstack1l1llll1_opy_ == bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᜘"):
            threading.current_thread().testStatus = bstack1l1llll1_opy_