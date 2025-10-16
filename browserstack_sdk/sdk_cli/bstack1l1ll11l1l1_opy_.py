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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import bstack111111lll1_opy_, bstack1lllllll1ll_opy_, bstack111111111l_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1111_opy_ import bstack111111ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1lllll11ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1llll1111ll_opy_, bstack1lll1ll111l_opy_, bstack1ll11l111l1_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1ll1l1l_opy_, bstack1ll11l1l111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1ll11l_opy_ = [bstack1ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᎯ"), bstack1ll11_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᎰ"), bstack1ll11_opy_ (u"ࠣࡥࡲࡲ࡫࡯ࡧࠣᎱ"), bstack1ll11_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࠥᎲ"), bstack1ll11_opy_ (u"ࠥࡴࡦࡺࡨࠣᎳ")]
bstack1ll111llll1_opy_ = bstack1ll11l1l111_opy_()
bstack1ll11l1ll1l_opy_ = bstack1ll11_opy_ (u"࡚ࠦࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠰ࠦᎴ")
bstack1l11ll111l1_opy_ = {
    bstack1ll11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡏࡴࡦ࡯ࠥᎵ"): bstack1l11l1ll11l_opy_,
    bstack1ll11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡐࡢࡥ࡮ࡥ࡬࡫ࠢᎶ"): bstack1l11l1ll11l_opy_,
    bstack1ll11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡎࡱࡧࡹࡱ࡫ࠢᎷ"): bstack1l11l1ll11l_opy_,
    bstack1ll11_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡅ࡯ࡥࡸࡹࠢᎸ"): bstack1l11l1ll11l_opy_,
    bstack1ll11_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡉࡹࡳࡩࡴࡪࡱࡱࠦᎹ"): bstack1l11l1ll11l_opy_
    + [
        bstack1ll11_opy_ (u"ࠥࡳࡷ࡯ࡧࡪࡰࡤࡰࡳࡧ࡭ࡦࠤᎺ"),
        bstack1ll11_opy_ (u"ࠦࡰ࡫ࡹࡸࡱࡵࡨࡸࠨᎻ"),
        bstack1ll11_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪ࡯࡮ࡧࡱࠥᎼ"),
        bstack1ll11_opy_ (u"ࠨ࡫ࡦࡻࡺࡳࡷࡪࡳࠣᎽ"),
        bstack1ll11_opy_ (u"ࠢࡤࡣ࡯ࡰࡸࡶࡥࡤࠤᎾ"),
        bstack1ll11_opy_ (u"ࠣࡥࡤࡰࡱࡵࡢ࡫ࠤᎿ"),
        bstack1ll11_opy_ (u"ࠤࡶࡸࡦࡸࡴࠣᏀ"),
        bstack1ll11_opy_ (u"ࠥࡷࡹࡵࡰࠣᏁ"),
        bstack1ll11_opy_ (u"ࠦࡩࡻࡲࡢࡶ࡬ࡳࡳࠨᏂ"),
        bstack1ll11_opy_ (u"ࠧࡽࡨࡦࡰࠥᏃ"),
    ],
    bstack1ll11_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴࡭ࡢ࡫ࡱ࠲ࡘ࡫ࡳࡴ࡫ࡲࡲࠧᏄ"): [bstack1ll11_opy_ (u"ࠢࡴࡶࡤࡶࡹࡶࡡࡵࡪࠥᏅ"), bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡹࡦࡢ࡫࡯ࡩࡩࠨᏆ"), bstack1ll11_opy_ (u"ࠤࡷࡩࡸࡺࡳࡤࡱ࡯ࡰࡪࡩࡴࡦࡦࠥᏇ"), bstack1ll11_opy_ (u"ࠥ࡭ࡹ࡫࡭ࡴࠤᏈ")],
    bstack1ll11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡨࡵ࡮ࡧ࡫ࡪ࠲ࡈࡵ࡮ࡧ࡫ࡪࠦᏉ"): [bstack1ll11_opy_ (u"ࠧ࡯࡮ࡷࡱࡦࡥࡹ࡯࡯࡯ࡡࡳࡥࡷࡧ࡭ࡴࠤᏊ"), bstack1ll11_opy_ (u"ࠨࡡࡳࡩࡶࠦᏋ")],
    bstack1ll11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠰ࡉ࡭ࡽࡺࡵࡳࡧࡇࡩ࡫ࠨᏌ"): [bstack1ll11_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᏍ"), bstack1ll11_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥᏎ"), bstack1ll11_opy_ (u"ࠥࡪࡺࡴࡣࠣᏏ"), bstack1ll11_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦᏐ"), bstack1ll11_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢᏑ"), bstack1ll11_opy_ (u"ࠨࡩࡥࡵࠥᏒ")],
    bstack1ll11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠰ࡖࡹࡧࡘࡥࡲࡷࡨࡷࡹࠨᏓ"): [bstack1ll11_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨᏔ"), bstack1ll11_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࠣᏕ"), bstack1ll11_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡡ࡬ࡲࡩ࡫ࡸࠣᏖ")],
    bstack1ll11_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡷࡻ࡮࡯ࡧࡵ࠲ࡈࡧ࡬࡭ࡋࡱࡪࡴࠨᏗ"): [bstack1ll11_opy_ (u"ࠧࡽࡨࡦࡰࠥᏘ"), bstack1ll11_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࠨᏙ")],
    bstack1ll11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣࡵ࡯࠳ࡹࡴࡳࡷࡦࡸࡺࡸࡥࡴ࠰ࡑࡳࡩ࡫ࡋࡦࡻࡺࡳࡷࡪࡳࠣᏚ"): [bstack1ll11_opy_ (u"ࠣࡰࡲࡨࡪࠨᏛ"), bstack1ll11_opy_ (u"ࠤࡳࡥࡷ࡫࡮ࡵࠤᏜ")],
    bstack1ll11_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦࡸ࡫࠯ࡵࡷࡶࡺࡩࡴࡶࡴࡨࡷ࠳ࡓࡡࡳ࡭ࠥᏝ"): [bstack1ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᏞ"), bstack1ll11_opy_ (u"ࠧࡧࡲࡨࡵࠥᏟ"), bstack1ll11_opy_ (u"ࠨ࡫ࡸࡣࡵ࡫ࡸࠨᏠ")],
}
_1ll11l11l11_opy_ = set()
class bstack1l1l1l11lll_opy_(bstack111111ll11_opy_):
    bstack1l11l1ll1ll_opy_ = bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡥࡧࡧࡵࡶࡪࡪࠢᏡ")
    bstack1l11ll1ll1l_opy_ = bstack1ll11_opy_ (u"ࠣࡋࡑࡊࡔࠨᏢ")
    bstack1l11ll11l1l_opy_ = bstack1ll11_opy_ (u"ࠤࡈࡖࡗࡕࡒࠣᏣ")
    bstack1l11l11ll1l_opy_: Callable
    bstack1l11l1l1l11_opy_: Callable
    def __init__(self, bstack1l11llll1l1_opy_, bstack1ll1llll111_opy_):
        super().__init__()
        self.bstack1l11ll11l11_opy_ = bstack1ll1llll111_opy_
        if os.getenv(bstack1ll11_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡒ࠵࠶࡟ࠢᏤ"), bstack1ll11_opy_ (u"ࠦ࠶ࠨᏥ")) != bstack1ll11_opy_ (u"ࠧ࠷ࠢᏦ") or not self.is_enabled():
            self.logger.warning(bstack1ll11_opy_ (u"ࠨࠢᏧ") + str(self.__class__.__name__) + bstack1ll11_opy_ (u"ࠢࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦࠥᏨ"))
            return
        TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.PRE), self.bstack1llll1l1111_opy_)
        TestFramework.bstack11111111l1_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l1ll1l_opy_)
        for event in bstack1llll111l1l_opy_:
            for state in bstack1lll1ll111l_opy_:
                TestFramework.bstack11111111l1_opy_((event, state), self.bstack1l11l111lll_opy_)
        bstack1l11llll1l1_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_, bstack111111111l_opy_.POST), self.bstack1l11l1ll1l1_opy_)
        self.bstack1l11l11ll1l_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l111l1l_opy_(bstack1l1l1l11lll_opy_.bstack1l11ll1ll1l_opy_, self.bstack1l11l11ll1l_opy_)
        self.bstack1l11l1l1l11_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l111l1l_opy_(bstack1l1l1l11lll_opy_.bstack1l11ll11l1l_opy_, self.bstack1l11l1l1l11_opy_)
        self.bstack1l11l11lll1_opy_ = builtins.print
        builtins.print = self.bstack1l11l1l1l1l_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll11ll1ll1_opy_() and instance:
            bstack1l11ll11lll_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1llll1l1ll1_opy_
            if test_framework_state == bstack1llll111l1l_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1llll111l1l_opy_.LOG:
                bstack11l1lll1l_opy_ = datetime.now()
                entries = f.bstack1ll1ll111l1_opy_(instance, bstack1llll1l1ll1_opy_)
                if entries:
                    self.bstack1ll1l1ll11l_opy_(instance, entries)
                    instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࠣᏩ"), datetime.now() - bstack11l1lll1l_opy_)
                    f.bstack1ll111l1111_opy_(instance, bstack1llll1l1ll1_opy_)
                instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠤࡲ࠵࠶ࡿ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧᏪ"), datetime.now() - bstack1l11ll11lll_opy_)
                return # do not send this event with the bstack1l11ll1ll11_opy_ bstack1l11ll11111_opy_
            elif (
                test_framework_state == bstack1llll111l1l_opy_.TEST
                and test_hook_state == bstack1lll1ll111l_opy_.POST
                and not f.bstack1111111lll_opy_(instance, TestFramework.bstack1l1lllll111_opy_)
            ):
                self.logger.warning(bstack1ll11_opy_ (u"ࠥࡨࡷࡵࡰࡱ࡫ࡱ࡫ࠥࡪࡵࡦࠢࡷࡳࠥࡲࡡࡤ࡭ࠣࡳ࡫ࠦࡲࡦࡵࡸࡰࡹࡹࠠࠣᏫ") + str(TestFramework.bstack1111111lll_opy_(instance, TestFramework.bstack1l1lllll111_opy_)) + bstack1ll11_opy_ (u"ࠦࠧᏬ"))
                f.bstack1llll1ll1ll_opy_(instance, bstack1l1l1l11lll_opy_.bstack1l11l1ll1ll_opy_, True)
                return # do not send this event bstack1l11ll1l11l_opy_ bstack1l11l11l1l1_opy_
            elif (
                f.get_state(instance, bstack1l1l1l11lll_opy_.bstack1l11l1ll1ll_opy_, False)
                and test_framework_state == bstack1llll111l1l_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1ll111l_opy_.POST
                and f.bstack1111111lll_opy_(instance, TestFramework.bstack1l1lllll111_opy_)
            ):
                self.logger.warning(bstack1ll11_opy_ (u"ࠧ࡯࡮࡫ࡧࡦࡸ࡮ࡴࡧࠡࡖࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡔࡶࡤࡸࡪ࠴ࡔࡆࡕࡗ࠰࡚ࠥࡥࡴࡶࡋࡳࡴࡱࡓࡵࡣࡷࡩ࠳ࡖࡏࡔࡖࠣࠦᏭ") + str(TestFramework.bstack1111111lll_opy_(instance, TestFramework.bstack1l1lllll111_opy_)) + bstack1ll11_opy_ (u"ࠨࠢᏮ"))
                self.bstack1l11l111lll_opy_(f, instance, (bstack1llll111l1l_opy_.TEST, bstack1lll1ll111l_opy_.POST), *args, **kwargs)
            bstack11l1lll1l_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l1111l1_opy_ = sorted(
                filter(lambda x: x.get(bstack1ll11_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᏯ"), None), data.pop(bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᏰ"), {}).values()),
                key=lambda x: x[bstack1ll11_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᏱ")],
            )
            if bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_ in data:
                data.pop(bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_)
            data.update({bstack1ll11_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᏲ"): bstack1l11l1111l1_opy_})
            instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠦ࡯ࡹ࡯࡯࠼ࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᏳ"), datetime.now() - bstack11l1lll1l_opy_)
            bstack11l1lll1l_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l11l11l_opy_)
            instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠧࡰࡳࡰࡰ࠽ࡳࡳࡥࡡ࡭࡮ࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺࡳࠣᏴ"), datetime.now() - bstack11l1lll1l_opy_)
            self.bstack1l11ll11111_opy_(instance, bstack1llll1l1ll1_opy_, event_json=event_json)
            instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᏵ"), datetime.now() - bstack1l11ll11lll_opy_)
    def bstack1llll1l1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l111l1l_opy_ import bstack1llll1lllll_opy_
        bstack1ll1l1ll1l1_opy_ = bstack1llll1lllll_opy_.bstack1ll111lll1l_opy_(EVENTS.bstack111l111l11_opy_.value)
        self.bstack1l11ll11l11_opy_.bstack1lll1ll1ll1_opy_(instance, f, bstack1llll1l1ll1_opy_, *args, **kwargs)
        bstack1llll1lllll_opy_.end(EVENTS.bstack111l111l11_opy_.value, bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ᏶"), bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ᏷"), status=True, failure=None, test_name=None)
    def bstack1lll1l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11ll11l11_opy_.bstack1llll1l11l1_opy_(instance, f, bstack1llll1l1ll1_opy_, *args, **kwargs)
        self.bstack1l11l1l1ll1_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l1lll11_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1l11l1l1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111ll_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1ll11_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤ࡙࡫ࡳࡵࡕࡨࡷࡸ࡯࡯࡯ࡇࡹࡩࡳࡺࠠࡨࡔࡓࡇࠥࡩࡡ࡭࡮࠽ࠤࡓࡵࠠࡷࡣ࡯࡭ࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡥࡣࡷࡥࠧᏸ"))
            return
        bstack11l1lll1l_opy_ = datetime.now()
        try:
            r = self.bstack1llllll111l_opy_.TestSessionEvent(req)
            instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡫ࡶࡦࡰࡷࠦᏹ"), datetime.now() - bstack11l1lll1l_opy_)
            f.bstack1llll1ll1ll_opy_(instance, self.bstack1l11ll11l11_opy_.bstack1lll1ll1111_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1ll11_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᏺ") + str(r) + bstack1ll11_opy_ (u"ࠧࠨᏻ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᏼ") + str(e) + bstack1ll11_opy_ (u"ࠢࠣᏽ"))
            traceback.print_exc()
            raise e
    def bstack1l11l1ll1l1_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        _driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        _1l11l1l111l_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllll11ll1_opy_.bstack1l1lll1lll1_opy_(method_name):
            return
        if f.bstack1l1lll11ll1_opy_(*args) == bstack1lllll11ll1_opy_.bstack1l11l11l1ll_opy_:
            bstack1l11ll11lll_opy_ = datetime.now()
            screenshot = result.get(bstack1ll11_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢ᏾"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1ll11_opy_ (u"ࠤ࡬ࡲࡻࡧ࡬ࡪࡦࠣࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠠࡪ࡯ࡤ࡫ࡪࠦࡢࡢࡵࡨ࠺࠹ࠦࡳࡵࡴࠥ᏿"))
                return
            bstack1ll11ll1lll_opy_ = self.bstack1l11l11llll_opy_(instance)
            if bstack1ll11ll1lll_opy_:
                entry = bstack1ll11l111l1_opy_(TestFramework.bstack1l11ll1l111_opy_, screenshot)
                self.bstack1ll1l1ll11l_opy_(bstack1ll11ll1lll_opy_, [entry])
                instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡩࡽ࡫ࡣࡶࡶࡨࠦ᐀"), datetime.now() - bstack1l11ll11lll_opy_)
            else:
                self.logger.warning(bstack1ll11_opy_ (u"ࠦࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡸࡪࡹࡴࠡࡨࡲࡶࠥࡽࡨࡪࡥ࡫ࠤࡹ࡮ࡩࡴࠢࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠦࡷࡢࡵࠣࡸࡦࡱࡥ࡯ࠢࡥࡽࠥࡪࡲࡪࡸࡨࡶࡂࠦࡻࡾࠤᐁ").format(instance.ref()))
        event = {}
        bstack1ll11ll1lll_opy_ = self.bstack1l11l11llll_opy_(instance)
        if bstack1ll11ll1lll_opy_:
            self.bstack1l11l1l1lll_opy_(event, bstack1ll11ll1lll_opy_)
            if event.get(bstack1ll11_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᐂ")):
                self.bstack1ll1l1ll11l_opy_(bstack1ll11ll1lll_opy_, event[bstack1ll11_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᐃ")])
            else:
                self.logger.debug(bstack1ll11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦ࡬ࡰࡩࡶࠤ࡫ࡵࡲࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥ࡫ࡶࡦࡰࡷࠦᐄ"))
    @measure(event_name=EVENTS.bstack1l11ll11ll1_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1ll1l1ll11l_opy_(
        self,
        bstack1ll11ll1lll_opy_: bstack1llll1111ll_opy_,
        entries: List[bstack1ll11l111l1_opy_],
    ):
        self.bstack1111111l1l_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1lllll111ll_opy_)
        req.execution_context.hash = str(bstack1ll11ll1lll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11ll1lll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11ll1lll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1llll111l11_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1llll1l1l11_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1lll1l11ll1_opy_)
            log_entry.test_framework_state = bstack1ll11ll1lll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1ll11_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᐅ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1ll11_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᐆ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1l1l1l_opy_
                log_entry.file_path = entry.bstack1lll111_opy_
        def bstack1ll111l1l11_opy_():
            bstack11l1lll1l_opy_ = datetime.now()
            try:
                self.bstack1llllll111l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11ll1l111_opy_:
                    bstack1ll11ll1lll_opy_.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᐇ"), datetime.now() - bstack11l1lll1l_opy_)
                elif entry.kind == TestFramework.bstack1l11l1l11l1_opy_:
                    bstack1ll11ll1lll_opy_.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠣᐈ"), datetime.now() - bstack11l1lll1l_opy_)
                else:
                    bstack1ll11ll1lll_opy_.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡲ࡯ࡨࠤᐉ"), datetime.now() - bstack11l1lll1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1ll11_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᐊ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll111l1l11_opy_)
    @measure(event_name=EVENTS.bstack1l11ll1111l_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1l11ll11111_opy_(
        self,
        instance: bstack1llll1111ll_opy_,
        bstack1llll1l1ll1_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1ll111l_opy_],
        event_json=None,
    ):
        self.bstack1111111l1l_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll111ll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1l1l11_opy_)
        req.test_framework_state = bstack1llll1l1ll1_opy_[0].name
        req.test_hook_state = bstack1llll1l1ll1_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll11lll111_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll1l1l1ll1_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l11l11l_opy_)).encode(bstack1ll11_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᐋ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll111l1l11_opy_():
            bstack11l1lll1l_opy_ = datetime.now()
            try:
                self.bstack1llllll111l_opy_.TestFrameworkEvent(req)
                instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤ࡫ࡶࡦࡰࡷࠦᐌ"), datetime.now() - bstack11l1lll1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1ll11_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᐍ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll1l11111_opy_.enqueue(bstack1ll111l1l11_opy_)
    def bstack1l11l11llll_opy_(self, instance: bstack111111lll1_opy_):
        bstack1l11l111l11_opy_ = TestFramework.bstack1l11ll111ll_opy_(instance.context)
        for t in bstack1l11l111l11_opy_:
            bstack1lll11llll1_opy_ = TestFramework.get_state(t, bstack1lll11lll1l_opy_.bstack1lll1ll11l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11llll1_opy_):
                return t
    def bstack1l11l1l1111_opy_(self, message):
        self.bstack1l11l11ll1l_opy_(message + bstack1ll11_opy_ (u"ࠥࡠࡳࠨᐎ"))
    def log_error(self, message):
        self.bstack1l11l1l1l11_opy_(message + bstack1ll11_opy_ (u"ࠦࡡࡴࠢᐏ"))
    def bstack1l11l111l1l_opy_(self, level, original_func):
        def bstack1l11l11111l_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1ll11_opy_ (u"ࠧࡋࡶࡦࡰࡷࡈ࡮ࡹࡰࡢࡶࡦ࡬ࡪࡸࡍࡰࡦࡸࡰࡪࠨᐐ") in message or bstack1ll11_opy_ (u"ࠨ࡛ࡔࡆࡎࡇࡑࡏ࡝ࠣᐑ") in message or bstack1ll11_opy_ (u"ࠢ࡜࡙ࡨࡦࡉࡸࡩࡷࡧࡵࡑࡴࡪࡵ࡭ࡧࡠࠦᐒ") in message:
                return return_value
            bstack1l11l111l11_opy_ = TestFramework.bstack1l11l111ll1_opy_()
            if not bstack1l11l111l11_opy_:
                return return_value
            bstack1ll11ll1lll_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l111l11_opy_
                    if TestFramework.bstack1111111lll_opy_(instance, TestFramework.bstack1lll1l11ll1_opy_)
                ),
                None,
            )
            if not bstack1ll11ll1lll_opy_:
                return return_value
            entry = bstack1ll11l111l1_opy_(TestFramework.bstack1ll1l11ll1l_opy_, message, level)
            self.bstack1ll1l1ll11l_opy_(bstack1ll11ll1lll_opy_, [entry])
            return return_value
        return bstack1l11l11111l_opy_
    def bstack1l11l1l1l1l_opy_(self):
        def bstack1l11l11l111_opy_(*args, **kwargs):
            try:
                self.bstack1l11l11lll1_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1ll11_opy_ (u"ࠨࠢࠪᐓ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1ll11_opy_ (u"ࠤࡈࡺࡪࡴࡴࡅ࡫ࡶࡴࡦࡺࡣࡩࡧࡵࡑࡴࡪࡵ࡭ࡧࠥᐔ") in message:
                    return
                bstack1l11l111l11_opy_ = TestFramework.bstack1l11l111ll1_opy_()
                if not bstack1l11l111l11_opy_:
                    return
                bstack1ll11ll1lll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l111l11_opy_
                        if TestFramework.bstack1111111lll_opy_(instance, TestFramework.bstack1lll1l11ll1_opy_)
                    ),
                    None,
                )
                if not bstack1ll11ll1lll_opy_:
                    return
                entry = bstack1ll11l111l1_opy_(TestFramework.bstack1ll1l11ll1l_opy_, message, bstack1l1l1l11lll_opy_.bstack1l11ll1ll1l_opy_)
                self.bstack1ll1l1ll11l_opy_(bstack1ll11ll1lll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l11lll1_opy_(bstack1lll1llllll_opy_ (u"ࠥ࡟ࡊࡼࡥ࡯ࡶࡇ࡭ࡸࡶࡡࡵࡥ࡫ࡩࡷࡓ࡯ࡥࡷ࡯ࡩࡢࠦࡌࡰࡩࠣࡧࡦࡶࡴࡶࡴࡨࠤࡪࡸࡲࡰࡴ࠽ࠤࢀ࡫ࡽࠣᐕ"))
                except:
                    pass
        return bstack1l11l11l111_opy_
    def bstack1l11l1l1lll_opy_(self, event: dict, instance=None) -> None:
        global _1ll11l11l11_opy_
        levels = [bstack1ll11_opy_ (u"࡙ࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢᐖ"), bstack1ll11_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᐗ")]
        bstack1l11l1llll1_opy_ = bstack1ll11_opy_ (u"ࠨࠢᐘ")
        if instance is not None:
            try:
                bstack1l11l1llll1_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll1l11ll1_opy_)
            except Exception as e:
                self.logger.warning(bstack1ll11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡶࡷ࡬ࡨࠥ࡬ࡲࡰ࡯ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠧᐙ").format(e))
        bstack1l11l1ll111_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᐚ")]
                bstack1ll11l1lll1_opy_ = os.path.join(bstack1ll111llll1_opy_, (bstack1ll11l1ll1l_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll11l1lll1_opy_):
                    self.logger.debug(bstack1ll11_opy_ (u"ࠤࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡴ࡯ࡵࠢࡳࡶࡪࡹࡥ࡯ࡶࠣࡪࡴࡸࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡙࡫ࡳࡵࠢࡤࡲࡩࠦࡂࡶ࡫࡯ࡨࠥࡲࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡾࢁࠧᐛ").format(bstack1ll11l1lll1_opy_))
                    continue
                file_names = os.listdir(bstack1ll11l1lll1_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll11l1lll1_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll11l11l11_opy_:
                        self.logger.info(bstack1ll11_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᐜ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l1111ll_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l1111ll_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1ll11_opy_ (u"࡙ࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢᐝ"):
                                entry = bstack1ll11l111l1_opy_(
                                    kind=bstack1ll11_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᐞ"),
                                    message=bstack1ll11_opy_ (u"ࠨࠢᐟ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l1l1l1l_opy_=file_size,
                                    bstack1l1lllllll1_opy_=bstack1ll11_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᐠ"),
                                    bstack1lll111_opy_=os.path.abspath(file_path),
                                    bstack11lll1lll1_opy_=bstack1l11l1llll1_opy_
                                )
                            elif level == bstack1ll11_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᐡ"):
                                entry = bstack1ll11l111l1_opy_(
                                    kind=bstack1ll11_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᐢ"),
                                    message=bstack1ll11_opy_ (u"ࠥࠦᐣ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l1l1l1l_opy_=file_size,
                                    bstack1l1lllllll1_opy_=bstack1ll11_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦᐤ"),
                                    bstack1lll111_opy_=os.path.abspath(file_path),
                                    bstack1ll11llllll_opy_=bstack1l11l1llll1_opy_
                                )
                            bstack1l11l1ll111_opy_.append(entry)
                            _1ll11l11l11_opy_.add(abs_path)
                        except Exception as bstack1l11l1lllll_opy_:
                            self.logger.error(bstack1ll11_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡴࡤ࡭ࡸ࡫ࡤࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡽࢀࠦᐥ").format(bstack1l11l1lllll_opy_))
        except Exception as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡵࡥ࡮ࡹࡥࡥࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡾࢁࠧᐦ").format(e))
        event[bstack1ll11_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᐧ")] = bstack1l11l1ll111_opy_
class bstack1l11l11l11l_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l1lll1l_opy_ = set()
        kwargs[bstack1ll11_opy_ (u"ࠣࡵ࡮࡭ࡵࡱࡥࡺࡵࠥᐨ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11ll1l1ll_opy_(obj, self.bstack1l11l1lll1l_opy_)
def bstack1l11l11ll11_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11ll1l1ll_opy_(obj, bstack1l11l1lll1l_opy_=None, max_depth=3):
    if bstack1l11l1lll1l_opy_ is None:
        bstack1l11l1lll1l_opy_ = set()
    if id(obj) in bstack1l11l1lll1l_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l1lll1l_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11ll1l1l1_opy_ = TestFramework.bstack1ll1111ll1l_opy_(obj)
    bstack1l11l1l11ll_opy_ = next((k.lower() in bstack1l11ll1l1l1_opy_.lower() for k in bstack1l11ll111l1_opy_.keys()), None)
    if bstack1l11l1l11ll_opy_:
        obj = TestFramework.bstack1ll11lll1l1_opy_(obj, bstack1l11ll111l1_opy_[bstack1l11l1l11ll_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1ll11_opy_ (u"ࠤࡢࡣࡸࡲ࡯ࡵࡵࡢࡣࠧᐩ")):
            keys = getattr(obj, bstack1ll11_opy_ (u"ࠥࡣࡤࡹ࡬ࡰࡶࡶࡣࡤࠨᐪ"), [])
        elif hasattr(obj, bstack1ll11_opy_ (u"ࠦࡤࡥࡤࡪࡥࡷࡣࡤࠨᐫ")):
            keys = getattr(obj, bstack1ll11_opy_ (u"ࠧࡥ࡟ࡥ࡫ࡦࡸࡤࡥࠢᐬ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1ll11_opy_ (u"ࠨ࡟ࠣᐭ"))}
        if not obj and bstack1l11ll1l1l1_opy_ == bstack1ll11_opy_ (u"ࠢࡱࡣࡷ࡬ࡱ࡯ࡢ࠯ࡒࡲࡷ࡮ࡾࡐࡢࡶ࡫ࠦᐮ"):
            obj = {bstack1ll11_opy_ (u"ࠣࡲࡤࡸ࡭ࠨᐯ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l11ll11_opy_(key) or str(key).startswith(bstack1ll11_opy_ (u"ࠤࡢࠦᐰ")):
            continue
        if value is not None and bstack1l11l11ll11_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11ll1l1ll_opy_(value, bstack1l11l1lll1l_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11ll1l1ll_opy_(o, bstack1l11l1lll1l_opy_, max_depth) for o in value]))
    return result or None