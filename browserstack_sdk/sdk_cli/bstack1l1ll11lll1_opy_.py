# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import bstack111111l111_opy_, bstack1111111l11_opy_, bstack1llllll1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll11llll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1lllll1ll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll1l_opy_, bstack1llll1l1l11_opy_, bstack1lll1llll1l_opy_, bstack1ll111l1l1l_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1l1llll_opy_, bstack1ll111l11l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11ll1l1l1_opy_ = [bstack1l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᎲ"), bstack1l_opy_ (u"ࠥࡴࡦࡸࡥ࡯ࡶࠥᎳ"), bstack1l_opy_ (u"ࠦࡨࡵ࡮ࡧ࡫ࡪࠦᎴ"), bstack1l_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࠨᎵ"), bstack1l_opy_ (u"ࠨࡰࡢࡶ࡫ࠦᎶ")]
bstack1ll11ll1l1l_opy_ = bstack1ll111l11l1_opy_()
bstack1ll111ll111_opy_ = bstack1l_opy_ (u"ࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢᎷ")
bstack1l11l1ll1ll_opy_ = {
    bstack1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡋࡷࡩࡲࠨᎸ"): bstack1l11ll1l1l1_opy_,
    bstack1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡓࡥࡨࡱࡡࡨࡧࠥᎹ"): bstack1l11ll1l1l1_opy_,
    bstack1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡑࡴࡪࡵ࡭ࡧࠥᎺ"): bstack1l11ll1l1l1_opy_,
    bstack1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡈࡲࡡࡴࡵࠥᎻ"): bstack1l11ll1l1l1_opy_,
    bstack1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡌࡵ࡯ࡥࡷ࡭ࡴࡴࠢᎼ"): bstack1l11ll1l1l1_opy_
    + [
        bstack1l_opy_ (u"ࠨ࡯ࡳ࡫ࡪ࡭ࡳࡧ࡬࡯ࡣࡰࡩࠧᎽ"),
        bstack1l_opy_ (u"ࠢ࡬ࡧࡼࡻࡴࡸࡤࡴࠤᎾ"),
        bstack1l_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦ࡫ࡱࡪࡴࠨᎿ"),
        bstack1l_opy_ (u"ࠤ࡮ࡩࡾࡽ࡯ࡳࡦࡶࠦᏀ"),
        bstack1l_opy_ (u"ࠥࡧࡦࡲ࡬ࡴࡲࡨࡧࠧᏁ"),
        bstack1l_opy_ (u"ࠦࡨࡧ࡬࡭ࡱࡥ࡮ࠧᏂ"),
        bstack1l_opy_ (u"ࠧࡹࡴࡢࡴࡷࠦᏃ"),
        bstack1l_opy_ (u"ࠨࡳࡵࡱࡳࠦᏄ"),
        bstack1l_opy_ (u"ࠢࡥࡷࡵࡥࡹ࡯࡯࡯ࠤᏅ"),
        bstack1l_opy_ (u"ࠣࡹ࡫ࡩࡳࠨᏆ"),
    ],
    bstack1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡰࡥ࡮ࡴ࠮ࡔࡧࡶࡷ࡮ࡵ࡮ࠣᏇ"): [bstack1l_opy_ (u"ࠥࡷࡹࡧࡲࡵࡲࡤࡸ࡭ࠨᏈ"), bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࡩࡥ࡮ࡲࡥࡥࠤᏉ"), bstack1l_opy_ (u"ࠧࡺࡥࡴࡶࡶࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠨᏊ"), bstack1l_opy_ (u"ࠨࡩࡵࡧࡰࡷࠧᏋ")],
    bstack1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡤࡱࡱࡪ࡮࡭࠮ࡄࡱࡱࡪ࡮࡭ࠢᏌ"): [bstack1l_opy_ (u"ࠣ࡫ࡱࡺࡴࡩࡡࡵ࡫ࡲࡲࡤࡶࡡࡳࡣࡰࡷࠧᏍ"), bstack1l_opy_ (u"ࠤࡤࡶ࡬ࡹࠢᏎ")],
    bstack1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡪ࡮ࡾࡴࡶࡴࡨࡷ࠳ࡌࡩࡹࡶࡸࡶࡪࡊࡥࡧࠤᏏ"): [bstack1l_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᏐ"), bstack1l_opy_ (u"ࠧࡧࡲࡨࡰࡤࡱࡪࠨᏑ"), bstack1l_opy_ (u"ࠨࡦࡶࡰࡦࠦᏒ"), bstack1l_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢᏓ"), bstack1l_opy_ (u"ࠣࡷࡱ࡭ࡹࡺࡥࡴࡶࠥᏔ"), bstack1l_opy_ (u"ࠤ࡬ࡨࡸࠨᏕ")],
    bstack1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡪ࡮ࡾࡴࡶࡴࡨࡷ࠳࡙ࡵࡣࡔࡨࡵࡺ࡫ࡳࡵࠤᏖ"): [bstack1l_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࠤᏗ"), bstack1l_opy_ (u"ࠧࡶࡡࡳࡣࡰࠦᏘ"), bstack1l_opy_ (u"ࠨࡰࡢࡴࡤࡱࡤ࡯࡮ࡥࡧࡻࠦᏙ")],
    bstack1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡳࡷࡱࡲࡪࡸ࠮ࡄࡣ࡯ࡰࡎࡴࡦࡰࠤᏚ"): [bstack1l_opy_ (u"ࠣࡹ࡫ࡩࡳࠨᏛ"), bstack1l_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࠤᏜ")],
    bstack1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦࡸ࡫࠯ࡵࡷࡶࡺࡩࡴࡶࡴࡨࡷ࠳ࡔ࡯ࡥࡧࡎࡩࡾࡽ࡯ࡳࡦࡶࠦᏝ"): [bstack1l_opy_ (u"ࠦࡳࡵࡤࡦࠤᏞ"), bstack1l_opy_ (u"ࠧࡶࡡࡳࡧࡱࡸࠧᏟ")],
    bstack1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴࡭ࡢࡴ࡮࠲ࡸࡺࡲࡶࡥࡷࡹࡷ࡫ࡳ࠯ࡏࡤࡶࡰࠨᏠ"): [bstack1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᏡ"), bstack1l_opy_ (u"ࠣࡣࡵ࡫ࡸࠨᏢ"), bstack1l_opy_ (u"ࠤ࡮ࡻࡦࡸࡧࡴࠤᏣ")],
}
_1ll11l1l1ll_opy_ = set()
class bstack1l1l11ll1ll_opy_(bstack1llll1llll1_opy_):
    bstack1l11ll11111_opy_ = bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡨࡪࡪࡸࡲࡦࡦࠥᏤ")
    bstack1l11ll1111l_opy_ = bstack1l_opy_ (u"ࠦࡎࡔࡆࡐࠤᏥ")
    bstack1l11l1l1ll1_opy_ = bstack1l_opy_ (u"ࠧࡋࡒࡓࡑࡕࠦᏦ")
    bstack1l11l1llll1_opy_: Callable
    bstack1l11l1l1111_opy_: Callable
    def __init__(self, bstack1l1l11l1lll_opy_, bstack1ll1llll1l1_opy_):
        super().__init__()
        self.bstack1l11l11ll1l_opy_ = bstack1ll1llll1l1_opy_
        if os.getenv(bstack1l_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡕ࠱࠲࡛ࠥᏧ"), bstack1l_opy_ (u"ࠢ࠲ࠤᏨ")) != bstack1l_opy_ (u"ࠣ࠳ࠥᏩ") or not self.is_enabled():
            self.logger.warning(bstack1l_opy_ (u"ࠤࠥᏪ") + str(self.__class__.__name__) + bstack1l_opy_ (u"ࠥࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩࠨᏫ"))
            return
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.PRE), self.bstack1lll1lll1ll_opy_)
        TestFramework.bstack1lllll1111l_opy_((bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.POST), self.bstack1lll1l1l1ll_opy_)
        for event in bstack1lll1l1ll1l_opy_:
            for state in bstack1lll1llll1l_opy_:
                TestFramework.bstack1lllll1111l_opy_((event, state), self.bstack1l11l11l111_opy_)
        bstack1l1l11l1lll_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.POST), self.bstack1l11l1lll1l_opy_)
        self.bstack1l11l1llll1_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l111lll_opy_(bstack1l1l11ll1ll_opy_.bstack1l11ll1111l_opy_, self.bstack1l11l1llll1_opy_)
        self.bstack1l11l1l1111_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l111lll_opy_(bstack1l1l11ll1ll_opy_.bstack1l11l1l1ll1_opy_, self.bstack1l11l1l1111_opy_)
        self.bstack1l11ll11l1l_opy_ = builtins.print
        builtins.print = self.bstack1l11ll11lll_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll111lll11_opy_() and instance:
            bstack1l11l1l1l11_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllll1ll11_opy_
            if test_framework_state == bstack1lll1l1ll1l_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1l1ll1l_opy_.LOG:
                bstack1l1111lll_opy_ = datetime.now()
                entries = f.bstack1ll1l111ll1_opy_(instance, bstack1lllll1ll11_opy_)
                if entries:
                    self.bstack1ll1111l11l_opy_(instance, entries)
                    instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࠦᏬ"), datetime.now() - bstack1l1111lll_opy_)
                    f.bstack1ll111llll1_opy_(instance, bstack1lllll1ll11_opy_)
                instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠧࡵ࠱࠲ࡻ࠽ࡳࡳࡥࡡ࡭࡮ࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺࡳࠣᏭ"), datetime.now() - bstack1l11l1l1l11_opy_)
                return # do not send this event with the bstack1l11l1l111l_opy_ bstack1l11l1ll1l1_opy_
            elif (
                test_framework_state == bstack1lll1l1ll1l_opy_.TEST
                and test_hook_state == bstack1lll1llll1l_opy_.POST
                and not f.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_)
            ):
                self.logger.warning(bstack1l_opy_ (u"ࠨࡤࡳࡱࡳࡴ࡮ࡴࡧࠡࡦࡸࡩࠥࡺ࡯ࠡ࡮ࡤࡧࡰࠦ࡯ࡧࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࠦᏮ") + str(TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_)) + bstack1l_opy_ (u"ࠢࠣᏯ"))
                f.bstack1lllll11ll1_opy_(instance, bstack1l1l11ll1ll_opy_.bstack1l11ll11111_opy_, True)
                return # do not send this event bstack1l11l1l1l1l_opy_ bstack1l11ll1l1ll_opy_
            elif (
                f.get_state(instance, bstack1l1l11ll1ll_opy_.bstack1l11ll11111_opy_, False)
                and test_framework_state == bstack1lll1l1ll1l_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1llll1l_opy_.POST
                and f.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_)
            ):
                self.logger.warning(bstack1l_opy_ (u"ࠣ࡫ࡱ࡮ࡪࡩࡴࡪࡰࡪࠤ࡙࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡗࡉࡘ࡚ࠬࠡࡖࡨࡷࡹࡎ࡯ࡰ࡭ࡖࡸࡦࡺࡥ࠯ࡒࡒࡗ࡙ࠦࠢᏰ") + str(TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1l111l_opy_)) + bstack1l_opy_ (u"ࠤࠥᏱ"))
                self.bstack1l11l11l111_opy_(f, instance, (bstack1lll1l1ll1l_opy_.TEST, bstack1lll1llll1l_opy_.POST), *args, **kwargs)
            bstack1l1111lll_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l1lllll_opy_ = sorted(
                filter(lambda x: x.get(bstack1l_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᏲ"), None), data.pop(bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᏳ"), {}).values()),
                key=lambda x: x[bstack1l_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᏴ")],
            )
            if bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_ in data:
                data.pop(bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_)
            data.update({bstack1l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᏵ"): bstack1l11l1lllll_opy_})
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠢ࡫ࡵࡲࡲ࠿ࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧ᏶"), datetime.now() - bstack1l1111lll_opy_)
            bstack1l1111lll_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l11l1ll_opy_)
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠣ࡬ࡶࡳࡳࡀ࡯࡯ࡡࡤࡰࡱࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶࡶࠦ᏷"), datetime.now() - bstack1l1111lll_opy_)
            self.bstack1l11l1ll1l1_opy_(instance, bstack1lllll1ll11_opy_, event_json=event_json)
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠤࡲ࠵࠶ࡿ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧᏸ"), datetime.now() - bstack1l11l1l1l11_opy_)
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
        bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack1ll11llllll_opy_(EVENTS.bstack1ll1l11lll_opy_.value)
        self.bstack1l11l11ll1l_opy_.bstack1lll1l1ll11_opy_(instance, f, bstack1lllll1ll11_opy_, *args, **kwargs)
        bstack1llll1l1lll_opy_.end(EVENTS.bstack1ll1l11lll_opy_.value, bstack1ll1l1lll11_opy_ + bstack1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᏹ"), bstack1ll1l1lll11_opy_ + bstack1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᏺ"), status=True, failure=None, test_name=None)
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l11ll1l_opy_.bstack1lll1ll11ll_opy_(instance, f, bstack1lllll1ll11_opy_, *args, **kwargs)
        self.bstack1l11l11l1l1_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l1111ll_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1l11l11l1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1l1l11_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1l_opy_ (u"࡙ࠧ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡕࡧࡶࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡊࡼࡥ࡯ࡶࠣ࡫ࡗࡖࡃࠡࡥࡤࡰࡱࡀࠠࡏࡱࠣࡺࡦࡲࡩࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡨࡦࡺࡡࠣᏻ"))
            return
        bstack1l1111lll_opy_ = datetime.now()
        try:
            r = self.bstack1llll1lll1l_opy_.TestSessionEvent(req)
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡧࡹࡩࡳࡺࠢᏼ"), datetime.now() - bstack1l1111lll_opy_)
            f.bstack1lllll11ll1_opy_(instance, self.bstack1l11l11ll1l_opy_.bstack1llll111l1l_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᏽ") + str(r) + bstack1l_opy_ (u"ࠣࠤ᏾"))
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢ᏿") + str(e) + bstack1l_opy_ (u"ࠥࠦ᐀"))
            traceback.print_exc()
            raise e
    def bstack1l11l1lll1l_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        _driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        _1l11l111ll1_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllll1ll1l_opy_.bstack1l1lll11lll_opy_(method_name):
            return
        if f.bstack1l1llll11l1_opy_(*args) == bstack1lllll1ll1l_opy_.bstack1l11ll11ll1_opy_:
            bstack1l11l1l1l11_opy_ = datetime.now()
            screenshot = result.get(bstack1l_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥᐁ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1l_opy_ (u"ࠧ࡯࡮ࡷࡣ࡯࡭ࡩࠦࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠣ࡭ࡲࡧࡧࡦࠢࡥࡥࡸ࡫࠶࠵ࠢࡶࡸࡷࠨᐂ"))
                return
            bstack1l1lllll1l1_opy_ = self.bstack1l11l111l11_opy_(instance)
            if bstack1l1lllll1l1_opy_:
                entry = bstack1ll111l1l1l_opy_(TestFramework.bstack1l11ll1l11l_opy_, screenshot)
                self.bstack1ll1111l11l_opy_(bstack1l1lllll1l1_opy_, [entry])
                instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡥࡹࡧࡦࡹࡹ࡫ࠢᐃ"), datetime.now() - bstack1l11l1l1l11_opy_)
            else:
                self.logger.warning(bstack1l_opy_ (u"ࠢࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡴࡦࡵࡷࠤ࡫ࡵࡲࠡࡹ࡫࡭ࡨ࡮ࠠࡵࡪ࡬ࡷࠥࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠢࡺࡥࡸࠦࡴࡢ࡭ࡨࡲࠥࡨࡹࠡࡦࡵ࡭ࡻ࡫ࡲ࠾ࠢࡾࢁࠧᐄ").format(instance.ref()))
        event = {}
        bstack1l1lllll1l1_opy_ = self.bstack1l11l111l11_opy_(instance)
        if bstack1l1lllll1l1_opy_:
            self.bstack1l11l11llll_opy_(event, bstack1l1lllll1l1_opy_)
            if event.get(bstack1l_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᐅ")):
                self.bstack1ll1111l11l_opy_(bstack1l1lllll1l1_opy_, event[bstack1l_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᐆ")])
            else:
                self.logger.debug(bstack1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢ࡯ࡳ࡬ࡹࠠࡧࡱࡵࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡧࡹࡩࡳࡺࠢᐇ"))
    @measure(event_name=EVENTS.bstack1l11l1111l1_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1ll1111l11l_opy_(
        self,
        bstack1l1lllll1l1_opy_: bstack1llll1l1l11_opy_,
        entries: List[bstack1ll111l1l1l_opy_],
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll1lllll_opy_)
        req.execution_context.hash = str(bstack1l1lllll1l1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1lllll1l1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1lllll1l1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll11111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1l1lllll1l1_opy_, TestFramework.bstack1llll11ll11_opy_)
            log_entry.test_framework_state = bstack1l1lllll1l1_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᐈ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᐉ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll111ll1l1_opy_
                log_entry.file_path = entry.bstack1ll11l1_opy_
        def bstack1ll1l1l1l1l_opy_():
            bstack1l1111lll_opy_ = datetime.now()
            try:
                self.bstack1llll1lll1l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11ll1l11l_opy_:
                    bstack1l1lllll1l1_opy_.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᐊ"), datetime.now() - bstack1l1111lll_opy_)
                elif entry.kind == TestFramework.bstack1l11l11111l_opy_:
                    bstack1l1lllll1l1_opy_.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦᐋ"), datetime.now() - bstack1l1111lll_opy_)
                else:
                    bstack1l1lllll1l1_opy_.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠ࡮ࡲ࡫ࠧᐌ"), datetime.now() - bstack1l1111lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᐍ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    @measure(event_name=EVENTS.bstack1l11ll1ll1l_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1l11l1ll1l1_opy_(
        self,
        instance: bstack1llll1l1l11_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1l1ll1l_opy_, bstack1lll1llll1l_opy_],
        event_json=None,
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1lllll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_state = bstack1lllll1ll11_opy_[0].name
        req.test_hook_state = bstack1lllll1ll11_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll11l1l1l1_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll1ll11111_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l11l1ll_opy_)).encode(bstack1l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᐎ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll1l1l1l1l_opy_():
            bstack1l1111lll_opy_ = datetime.now()
            try:
                self.bstack1llll1lll1l_opy_.TestFrameworkEvent(req)
                instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡧࡹࡩࡳࡺࠢᐏ"), datetime.now() - bstack1l1111lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᐐ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll1l1l1l1l_opy_)
    def bstack1l11l111l11_opy_(self, instance: bstack111111l111_opy_):
        bstack1l11l1ll11l_opy_ = TestFramework.bstack1l11ll111ll_opy_(instance.context)
        for t in bstack1l11l1ll11l_opy_:
            bstack1lll11l1l11_opy_ = TestFramework.get_state(t, bstack1lll11llll1_opy_.bstack1lll1l11l1l_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l1l11_opy_):
                return t
    def bstack1l11l1ll111_opy_(self, message):
        self.bstack1l11l1llll1_opy_(message + bstack1l_opy_ (u"ࠨ࡜࡯ࠤᐑ"))
    def log_error(self, message):
        self.bstack1l11l1l1111_opy_(message + bstack1l_opy_ (u"ࠢ࡝ࡰࠥᐒ"))
    def bstack1l11l111lll_opy_(self, level, original_func):
        def bstack1l11l11lll1_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1l_opy_ (u"ࠣࡇࡹࡩࡳࡺࡄࡪࡵࡳࡥࡹࡩࡨࡦࡴࡐࡳࡩࡻ࡬ࡦࠤᐓ") in message or bstack1l_opy_ (u"ࠤ࡞ࡗࡉࡑࡃࡍࡋࡠࠦᐔ") in message or bstack1l_opy_ (u"ࠥ࡟࡜࡫ࡢࡅࡴ࡬ࡺࡪࡸࡍࡰࡦࡸࡰࡪࡣࠢᐕ") in message:
                return return_value
            bstack1l11l1ll11l_opy_ = TestFramework.bstack1l11ll1l111_opy_()
            if not bstack1l11l1ll11l_opy_:
                return return_value
            bstack1l1lllll1l1_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l1ll11l_opy_
                    if TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1llll11ll11_opy_)
                ),
                None,
            )
            if not bstack1l1lllll1l1_opy_:
                return return_value
            entry = bstack1ll111l1l1l_opy_(TestFramework.bstack1ll11111l11_opy_, message, level)
            self.bstack1ll1111l11l_opy_(bstack1l1lllll1l1_opy_, [entry])
            return return_value
        return bstack1l11l11lll1_opy_
    def bstack1l11ll11lll_opy_(self):
        def bstack1l11l111l1l_opy_(*args, **kwargs):
            try:
                self.bstack1l11ll11l1l_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1l_opy_ (u"ࠫࠥ࠭ᐖ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1l_opy_ (u"ࠧࡋࡶࡦࡰࡷࡈ࡮ࡹࡰࡢࡶࡦ࡬ࡪࡸࡍࡰࡦࡸࡰࡪࠨᐗ") in message:
                    return
                bstack1l11l1ll11l_opy_ = TestFramework.bstack1l11ll1l111_opy_()
                if not bstack1l11l1ll11l_opy_:
                    return
                bstack1l1lllll1l1_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l1ll11l_opy_
                        if TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1llll11ll11_opy_)
                    ),
                    None,
                )
                if not bstack1l1lllll1l1_opy_:
                    return
                entry = bstack1ll111l1l1l_opy_(TestFramework.bstack1ll11111l11_opy_, message, bstack1l1l11ll1ll_opy_.bstack1l11ll1111l_opy_)
                self.bstack1ll1111l11l_opy_(bstack1l1lllll1l1_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11ll11l1l_opy_(bstack1lll1ll1l1l_opy_ (u"ࠨ࡛ࡆࡸࡨࡲࡹࡊࡩࡴࡲࡤࡸࡨ࡮ࡥࡳࡏࡲࡨࡺࡲࡥ࡞ࠢࡏࡳ࡬ࠦࡣࡢࡲࡷࡹࡷ࡫ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡧࢀࠦᐘ"))
                except:
                    pass
        return bstack1l11l111l1l_opy_
    def bstack1l11l11llll_opy_(self, event: dict, instance=None) -> None:
        global _1ll11l1l1ll_opy_
        levels = [bstack1l_opy_ (u"ࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥᐙ"), bstack1l_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᐚ")]
        bstack1l11l1l1lll_opy_ = bstack1l_opy_ (u"ࠤࠥᐛ")
        if instance is not None:
            try:
                bstack1l11l1l1lll_opy_ = TestFramework.get_state(instance, TestFramework.bstack1llll11ll11_opy_)
            except Exception as e:
                self.logger.warning(bstack1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡹࡺ࡯ࡤࠡࡨࡵࡳࡲࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠣᐜ").format(e))
        bstack1l11ll11l11_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᐝ")]
                bstack1ll1l1l11l1_opy_ = os.path.join(bstack1ll11ll1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1l1l11l1_opy_):
                    self.logger.debug(bstack1l_opy_ (u"ࠧࡊࡩࡳࡧࡦࡸࡴࡸࡹࠡࡰࡲࡸࠥࡶࡲࡦࡵࡨࡲࡹࠦࡦࡰࡴࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡕࡧࡶࡸࠥࡧ࡮ࡥࠢࡅࡹ࡮ࡲࡤࠡ࡮ࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࢁࡽࠣᐞ").format(bstack1ll1l1l11l1_opy_))
                    continue
                file_names = os.listdir(bstack1ll1l1l11l1_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1l1l11l1_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll11l1l1ll_opy_:
                        self.logger.info(bstack1l_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦᐟ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l1lll11_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l1lll11_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1l_opy_ (u"ࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥᐠ"):
                                entry = bstack1ll111l1l1l_opy_(
                                    kind=bstack1l_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᐡ"),
                                    message=bstack1l_opy_ (u"ࠤࠥᐢ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll111ll1l1_opy_=file_size,
                                    bstack1ll1l11l111_opy_=bstack1l_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥᐣ"),
                                    bstack1ll11l1_opy_=os.path.abspath(file_path),
                                    bstack11l1l1l11_opy_=bstack1l11l1l1lll_opy_
                                )
                            elif level == bstack1l_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᐤ"):
                                entry = bstack1ll111l1l1l_opy_(
                                    kind=bstack1l_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᐥ"),
                                    message=bstack1l_opy_ (u"ࠨࠢᐦ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll111ll1l1_opy_=file_size,
                                    bstack1ll1l11l111_opy_=bstack1l_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᐧ"),
                                    bstack1ll11l1_opy_=os.path.abspath(file_path),
                                    bstack1ll11ll1l11_opy_=bstack1l11l1l1lll_opy_
                                )
                            bstack1l11ll11l11_opy_.append(entry)
                            _1ll11l1l1ll_opy_.add(abs_path)
                        except Exception as bstack1l11l1l11ll_opy_:
                            self.logger.error(bstack1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡷࡧࡩࡴࡧࡧࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࢀࢃࠢᐨ").format(bstack1l11l1l11ll_opy_))
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡸࡡࡪࡵࡨࡨࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࢁࡽࠣᐩ").format(e))
        event[bstack1l_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᐪ")] = bstack1l11ll11l11_opy_
class bstack1l11l11l1ll_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l11ll11_opy_ = set()
        kwargs[bstack1l_opy_ (u"ࠦࡸࡱࡩࡱ࡭ࡨࡽࡸࠨᐫ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l11l11l_opy_(obj, self.bstack1l11l11ll11_opy_)
def bstack1l11ll111l1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l11l11l_opy_(obj, bstack1l11l11ll11_opy_=None, max_depth=3):
    if bstack1l11l11ll11_opy_ is None:
        bstack1l11l11ll11_opy_ = set()
    if id(obj) in bstack1l11l11ll11_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l11ll11_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11ll1ll11_opy_ = TestFramework.bstack1ll1l111111_opy_(obj)
    bstack1l11l1l11l1_opy_ = next((k.lower() in bstack1l11ll1ll11_opy_.lower() for k in bstack1l11l1ll1ll_opy_.keys()), None)
    if bstack1l11l1l11l1_opy_:
        obj = TestFramework.bstack1ll1l1l1ll1_opy_(obj, bstack1l11l1ll1ll_opy_[bstack1l11l1l11l1_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1l_opy_ (u"ࠧࡥ࡟ࡴ࡮ࡲࡸࡸࡥ࡟ࠣᐬ")):
            keys = getattr(obj, bstack1l_opy_ (u"ࠨ࡟ࡠࡵ࡯ࡳࡹࡹ࡟ࡠࠤᐭ"), [])
        elif hasattr(obj, bstack1l_opy_ (u"ࠢࡠࡡࡧ࡭ࡨࡺ࡟ࡠࠤᐮ")):
            keys = getattr(obj, bstack1l_opy_ (u"ࠣࡡࡢࡨ࡮ࡩࡴࡠࡡࠥᐯ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1l_opy_ (u"ࠤࡢࠦᐰ"))}
        if not obj and bstack1l11ll1ll11_opy_ == bstack1l_opy_ (u"ࠥࡴࡦࡺࡨ࡭࡫ࡥ࠲ࡕࡵࡳࡪࡺࡓࡥࡹ࡮ࠢᐱ"):
            obj = {bstack1l_opy_ (u"ࠦࡵࡧࡴࡩࠤᐲ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11ll111l1_opy_(key) or str(key).startswith(bstack1l_opy_ (u"ࠧࡥࠢᐳ")):
            continue
        if value is not None and bstack1l11ll111l1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l11l11l_opy_(value, bstack1l11l11ll11_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l11l11l_opy_(o, bstack1l11l11ll11_opy_, max_depth) for o in value]))
    return result or None