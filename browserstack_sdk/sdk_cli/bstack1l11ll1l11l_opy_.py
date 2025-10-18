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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import bstack1llll1l1111_opy_, bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll111ll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11l1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1lll_opy_, bstack1lll1l1ll1l_opy_, bstack1lll11lll1l_opy_, bstack1ll11ll1l1l_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1l11ll1_opy_, bstack1ll1l1ll111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1lll1l_opy_ = [bstack11l111_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᏒ"), bstack11l111_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᏓ"), bstack11l111_opy_ (u"ࠣࡥࡲࡲ࡫࡯ࡧࠣᏔ"), bstack11l111_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࠥᏕ"), bstack11l111_opy_ (u"ࠥࡴࡦࡺࡨࠣᏖ")]
bstack1ll1l1l1l1l_opy_ = bstack1ll1l1ll111_opy_()
bstack1ll111ll111_opy_ = bstack11l111_opy_ (u"࡚ࠦࡶ࡬ࡰࡣࡧࡩࡩࡇࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵ࠰ࠦᏗ")
bstack1l11l1lllll_opy_ = {
    bstack11l111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡏࡴࡦ࡯ࠥᏘ"): bstack1l11l1lll1l_opy_,
    bstack11l111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡐࡢࡥ࡮ࡥ࡬࡫ࠢᏙ"): bstack1l11l1lll1l_opy_,
    bstack11l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡎࡱࡧࡹࡱ࡫ࠢᏚ"): bstack1l11l1lll1l_opy_,
    bstack11l111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡅ࡯ࡥࡸࡹࠢᏛ"): bstack1l11l1lll1l_opy_,
    bstack11l111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡉࡹࡳࡩࡴࡪࡱࡱࠦᏜ"): bstack1l11l1lll1l_opy_
    + [
        bstack11l111_opy_ (u"ࠥࡳࡷ࡯ࡧࡪࡰࡤࡰࡳࡧ࡭ࡦࠤᏝ"),
        bstack11l111_opy_ (u"ࠦࡰ࡫ࡹࡸࡱࡵࡨࡸࠨᏞ"),
        bstack11l111_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪ࡯࡮ࡧࡱࠥᏟ"),
        bstack11l111_opy_ (u"ࠨ࡫ࡦࡻࡺࡳࡷࡪࡳࠣᏠ"),
        bstack11l111_opy_ (u"ࠢࡤࡣ࡯ࡰࡸࡶࡥࡤࠤᏡ"),
        bstack11l111_opy_ (u"ࠣࡥࡤࡰࡱࡵࡢ࡫ࠤᏢ"),
        bstack11l111_opy_ (u"ࠤࡶࡸࡦࡸࡴࠣᏣ"),
        bstack11l111_opy_ (u"ࠥࡷࡹࡵࡰࠣᏤ"),
        bstack11l111_opy_ (u"ࠦࡩࡻࡲࡢࡶ࡬ࡳࡳࠨᏥ"),
        bstack11l111_opy_ (u"ࠧࡽࡨࡦࡰࠥᏦ"),
    ],
    bstack11l111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴࡭ࡢ࡫ࡱ࠲ࡘ࡫ࡳࡴ࡫ࡲࡲࠧᏧ"): [bstack11l111_opy_ (u"ࠢࡴࡶࡤࡶࡹࡶࡡࡵࡪࠥᏨ"), bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡹࡦࡢ࡫࡯ࡩࡩࠨᏩ"), bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺࡳࡤࡱ࡯ࡰࡪࡩࡴࡦࡦࠥᏪ"), bstack11l111_opy_ (u"ࠥ࡭ࡹ࡫࡭ࡴࠤᏫ")],
    bstack11l111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡨࡵ࡮ࡧ࡫ࡪ࠲ࡈࡵ࡮ࡧ࡫ࡪࠦᏬ"): [bstack11l111_opy_ (u"ࠧ࡯࡮ࡷࡱࡦࡥࡹ࡯࡯࡯ࡡࡳࡥࡷࡧ࡭ࡴࠤᏭ"), bstack11l111_opy_ (u"ࠨࡡࡳࡩࡶࠦᏮ")],
    bstack11l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠰ࡉ࡭ࡽࡺࡵࡳࡧࡇࡩ࡫ࠨᏯ"): [bstack11l111_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢᏰ"), bstack11l111_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥᏱ"), bstack11l111_opy_ (u"ࠥࡪࡺࡴࡣࠣᏲ"), bstack11l111_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦᏳ"), bstack11l111_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢᏴ"), bstack11l111_opy_ (u"ࠨࡩࡥࡵࠥᏵ")],
    bstack11l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡧ࡫ࡻࡸࡺࡸࡥࡴ࠰ࡖࡹࡧࡘࡥࡲࡷࡨࡷࡹࠨ᏶"): [bstack11l111_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࠨ᏷"), bstack11l111_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࠣᏸ"), bstack11l111_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡡ࡬ࡲࡩ࡫ࡸࠣᏹ")],
    bstack11l111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡷࡻ࡮࡯ࡧࡵ࠲ࡈࡧ࡬࡭ࡋࡱࡪࡴࠨᏺ"): [bstack11l111_opy_ (u"ࠧࡽࡨࡦࡰࠥᏻ"), bstack11l111_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࠨᏼ")],
    bstack11l111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮࡮ࡣࡵ࡯࠳ࡹࡴࡳࡷࡦࡸࡺࡸࡥࡴ࠰ࡑࡳࡩ࡫ࡋࡦࡻࡺࡳࡷࡪࡳࠣᏽ"): [bstack11l111_opy_ (u"ࠣࡰࡲࡨࡪࠨ᏾"), bstack11l111_opy_ (u"ࠤࡳࡥࡷ࡫࡮ࡵࠤ᏿")],
    bstack11l111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦࡸ࡫࠯ࡵࡷࡶࡺࡩࡴࡶࡴࡨࡷ࠳ࡓࡡࡳ࡭ࠥ᐀"): [bstack11l111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᐁ"), bstack11l111_opy_ (u"ࠧࡧࡲࡨࡵࠥᐂ"), bstack11l111_opy_ (u"ࠨ࡫ࡸࡣࡵ࡫ࡸࠨᐃ")],
}
_1ll1l1l1l11_opy_ = set()
class bstack1l11lll1l1l_opy_(bstack1llll1l1l11_opy_):
    bstack1l11l111ll1_opy_ = bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡥࡧࡧࡵࡶࡪࡪࠢᐄ")
    bstack1l11l1111l1_opy_ = bstack11l111_opy_ (u"ࠣࡋࡑࡊࡔࠨᐅ")
    bstack1l11l1llll1_opy_ = bstack11l111_opy_ (u"ࠤࡈࡖࡗࡕࡒࠣᐆ")
    bstack1l111llllll_opy_: Callable
    bstack1l111lllll1_opy_: Callable
    def __init__(self, bstack1l1l1l111l1_opy_, bstack1ll1lll111l_opy_):
        super().__init__()
        self.bstack1l11l1l1l11_opy_ = bstack1ll1lll111l_opy_
        if os.getenv(bstack11l111_opy_ (u"ࠥࡗࡉࡑ࡟ࡄࡎࡌࡣࡋࡒࡁࡈࡡࡒ࠵࠶࡟ࠢᐇ"), bstack11l111_opy_ (u"ࠦ࠶ࠨᐈ")) != bstack11l111_opy_ (u"ࠧ࠷ࠢᐉ") or not self.is_enabled():
            self.logger.warning(bstack11l111_opy_ (u"ࠨࠢᐊ") + str(self.__class__.__name__) + bstack11l111_opy_ (u"ࠢࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦࠥᐋ"))
            return
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.PRE), self.bstack1llll111lll_opy_)
        TestFramework.bstack1lllllll11l_opy_((bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.POST), self.bstack1lll1llll1l_opy_)
        for event in bstack1lll1ll1lll_opy_:
            for state in bstack1lll11lll1l_opy_:
                TestFramework.bstack1lllllll11l_opy_((event, state), self.bstack1l11l1111ll_opy_)
        bstack1l1l1l111l1_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.POST), self.bstack1l111lll11l_opy_)
        self.bstack1l111llllll_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l1ll11l_opy_(bstack1l11lll1l1l_opy_.bstack1l11l1111l1_opy_, self.bstack1l111llllll_opy_)
        self.bstack1l111lllll1_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l1ll11l_opy_(bstack1l11lll1l1l_opy_.bstack1l11l1llll1_opy_, self.bstack1l111lllll1_opy_)
        self.bstack1l11l1ll111_opy_ = builtins.print
        builtins.print = self.bstack1l11l11l1l1_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll1l11ll11_opy_() and instance:
            bstack1l111llll11_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllll1ll11_opy_
            if test_framework_state == bstack1lll1ll1lll_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1ll1lll_opy_.LOG:
                bstack1l1ll1ll1_opy_ = datetime.now()
                entries = f.bstack1ll1l1l11ll_opy_(instance, bstack1lllll1ll11_opy_)
                if entries:
                    self.bstack1l1llll11ll_opy_(instance, entries)
                    instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࠣᐌ"), datetime.now() - bstack1l1ll1ll1_opy_)
                    f.bstack1ll1l11111l_opy_(instance, bstack1lllll1ll11_opy_)
                instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠤࡲ࠵࠶ࡿ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧᐍ"), datetime.now() - bstack1l111llll11_opy_)
                return # do not send this event with the bstack1l11ll11111_opy_ bstack1l11l111lll_opy_
            elif (
                test_framework_state == bstack1lll1ll1lll_opy_.TEST
                and test_hook_state == bstack1lll11lll1l_opy_.POST
                and not f.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_)
            ):
                self.logger.warning(bstack11l111_opy_ (u"ࠥࡨࡷࡵࡰࡱ࡫ࡱ࡫ࠥࡪࡵࡦࠢࡷࡳࠥࡲࡡࡤ࡭ࠣࡳ࡫ࠦࡲࡦࡵࡸࡰࡹࡹࠠࠣᐎ") + str(TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_)) + bstack11l111_opy_ (u"ࠦࠧᐏ"))
                f.bstack1llllllll1l_opy_(instance, bstack1l11lll1l1l_opy_.bstack1l11l111ll1_opy_, True)
                return # do not send this event bstack1l11l1l111l_opy_ bstack1l111ll1ll1_opy_
            elif (
                f.get_state(instance, bstack1l11lll1l1l_opy_.bstack1l11l111ll1_opy_, False)
                and test_framework_state == bstack1lll1ll1lll_opy_.LOG_REPORT
                and test_hook_state == bstack1lll11lll1l_opy_.POST
                and f.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_)
            ):
                self.logger.warning(bstack11l111_opy_ (u"ࠧ࡯࡮࡫ࡧࡦࡸ࡮ࡴࡧࠡࡖࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡔࡶࡤࡸࡪ࠴ࡔࡆࡕࡗ࠰࡚ࠥࡥࡴࡶࡋࡳࡴࡱࡓࡵࡣࡷࡩ࠳ࡖࡏࡔࡖࠣࠦᐐ") + str(TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1l1llll1ll1_opy_)) + bstack11l111_opy_ (u"ࠨࠢᐑ"))
                self.bstack1l11l1111ll_opy_(f, instance, (bstack1lll1ll1lll_opy_.TEST, bstack1lll11lll1l_opy_.POST), *args, **kwargs)
            bstack1l1ll1ll1_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l11ll11_opy_ = sorted(
                filter(lambda x: x.get(bstack11l111_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᐒ"), None), data.pop(bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᐓ"), {}).values()),
                key=lambda x: x[bstack11l111_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᐔ")],
            )
            if bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_ in data:
                data.pop(bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_)
            data.update({bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᐕ"): bstack1l11l11ll11_opy_})
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠦ࡯ࡹ࡯࡯࠼ࡷࡩࡸࡺ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠤᐖ"), datetime.now() - bstack1l1ll1ll1_opy_)
            bstack1l1ll1ll1_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l1l1lll_opy_)
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠧࡰࡳࡰࡰ࠽ࡳࡳࡥࡡ࡭࡮ࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺࡳࠣᐗ"), datetime.now() - bstack1l1ll1ll1_opy_)
            self.bstack1l11l111lll_opy_(instance, bstack1lllll1ll11_opy_, event_json=event_json)
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢ࡮࡯ࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴࡴࠤᐘ"), datetime.now() - bstack1l111llll11_opy_)
    def bstack1llll111lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
        bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack1ll11l11ll1_opy_(EVENTS.bstack111111lll1_opy_.value)
        self.bstack1l11l1l1l11_opy_.bstack1lll1ll111l_opy_(instance, f, bstack1lllll1ll11_opy_, *args, **kwargs)
        bstack1llll11ll11_opy_.end(EVENTS.bstack111111lll1_opy_.value, bstack1ll1l1l11l1_opy_ + bstack11l111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᐙ"), bstack1ll1l1l11l1_opy_ + bstack11l111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᐚ"), status=True, failure=None, test_name=None)
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l1l1l11_opy_.bstack1lll1llll11_opy_(instance, f, bstack1lllll1ll11_opy_, *args, **kwargs)
        self.bstack1l11ll1111l_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l11111l_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1l11ll1111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1ll1l_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack11l111_opy_ (u"ࠤࡖ࡯࡮ࡶࡰࡪࡰࡪࠤ࡙࡫ࡳࡵࡕࡨࡷࡸ࡯࡯࡯ࡇࡹࡩࡳࡺࠠࡨࡔࡓࡇࠥࡩࡡ࡭࡮࠽ࠤࡓࡵࠠࡷࡣ࡯࡭ࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡥࡣࡷࡥࠧᐛ"))
            return
        bstack1l1ll1ll1_opy_ = datetime.now()
        try:
            r = self.bstack1llllll1l11_opy_.TestSessionEvent(req)
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡫ࡶࡦࡰࡷࠦᐜ"), datetime.now() - bstack1l1ll1ll1_opy_)
            f.bstack1llllllll1l_opy_(instance, self.bstack1l11l1l1l11_opy_.bstack1llll111l1l_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11l111_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᐝ") + str(r) + bstack11l111_opy_ (u"ࠧࠨᐞ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᐟ") + str(e) + bstack11l111_opy_ (u"ࠢࠣᐠ"))
            traceback.print_exc()
            raise e
    def bstack1l111lll11l_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        _driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        _1l111lll1ll_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllll11l1l_opy_.bstack1l1ll1lllll_opy_(method_name):
            return
        if f.bstack1l1lll1111l_opy_(*args) == bstack1lllll11l1l_opy_.bstack1l11l1l11ll_opy_:
            bstack1l111llll11_opy_ = datetime.now()
            screenshot = result.get(bstack11l111_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢᐡ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack11l111_opy_ (u"ࠤ࡬ࡲࡻࡧ࡬ࡪࡦࠣࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠠࡪ࡯ࡤ࡫ࡪࠦࡢࡢࡵࡨ࠺࠹ࠦࡳࡵࡴࠥᐢ"))
                return
            bstack1ll111llll1_opy_ = self.bstack1l111lll111_opy_(instance)
            if bstack1ll111llll1_opy_:
                entry = bstack1ll11ll1l1l_opy_(TestFramework.bstack1l11l111111_opy_, screenshot)
                self.bstack1l1llll11ll_opy_(bstack1ll111llll1_opy_, [entry])
                instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠥࡳ࠶࠷ࡹ࠻ࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡩࡽ࡫ࡣࡶࡶࡨࠦᐣ"), datetime.now() - bstack1l111llll11_opy_)
            else:
                self.logger.warning(bstack11l111_opy_ (u"ࠦࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡸࡪࡹࡴࠡࡨࡲࡶࠥࡽࡨࡪࡥ࡫ࠤࡹ࡮ࡩࡴࠢࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠦࡷࡢࡵࠣࡸࡦࡱࡥ࡯ࠢࡥࡽࠥࡪࡲࡪࡸࡨࡶࡂࠦࡻࡾࠤᐤ").format(instance.ref()))
        event = {}
        bstack1ll111llll1_opy_ = self.bstack1l111lll111_opy_(instance)
        if bstack1ll111llll1_opy_:
            self.bstack1l11l1ll1ll_opy_(event, bstack1ll111llll1_opy_)
            if event.get(bstack11l111_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᐥ")):
                self.bstack1l1llll11ll_opy_(bstack1ll111llll1_opy_, event[bstack11l111_opy_ (u"ࠨ࡬ࡰࡩࡶࠦᐦ")])
            else:
                self.logger.debug(bstack11l111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦ࡬ࡰࡩࡶࠤ࡫ࡵࡲࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥ࡫ࡶࡦࡰࡷࠦᐧ"))
    @measure(event_name=EVENTS.bstack1l111llll1l_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1l1llll11ll_opy_(
        self,
        bstack1ll111llll1_opy_: bstack1lll1l1ll1l_opy_,
        entries: List[bstack1ll11ll1l1l_opy_],
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1llllllll11_opy_)
        req.execution_context.hash = str(bstack1ll111llll1_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111llll1_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111llll1_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1lll1l11l11_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1lll11ll111_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll111llll1_opy_, TestFramework.bstack1lll1lll1l1_opy_)
            log_entry.test_framework_state = bstack1ll111llll1_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l111_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᐨ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11l111_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᐩ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1llll11l1_opy_
                log_entry.file_path = entry.bstack11ll1ll_opy_
        def bstack1ll11l1l1l1_opy_():
            bstack1l1ll1ll1_opy_ = datetime.now()
            try:
                self.bstack1llllll1l11_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l111111_opy_:
                    bstack1ll111llll1_opy_.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᐪ"), datetime.now() - bstack1l1ll1ll1_opy_)
                elif entry.kind == TestFramework.bstack1l11l1l1l1l_opy_:
                    bstack1ll111llll1_opy_.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࡣࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠣᐫ"), datetime.now() - bstack1l1ll1ll1_opy_)
                else:
                    bstack1ll111llll1_opy_.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡲ࡯ࡨࠤᐬ"), datetime.now() - bstack1l1ll1ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l111_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᐭ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1ll11l1l1l1_opy_)
    @measure(event_name=EVENTS.bstack1l11l111l11_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1l11l111lll_opy_(
        self,
        instance: bstack1lll1l1ll1l_opy_,
        bstack1lllll1ll11_opy_: Tuple[bstack1lll1ll1lll_opy_, bstack1lll11lll1l_opy_],
        event_json=None,
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllll11_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11ll111_opy_)
        req.test_framework_state = bstack1lllll1ll11_opy_[0].name
        req.test_hook_state = bstack1lllll1ll11_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll1l111lll_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll11ll111l_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l1l1lll_opy_)).encode(bstack11l111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᐮ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll11l1l1l1_opy_():
            bstack1l1ll1ll1_opy_ = datetime.now()
            try:
                self.bstack1llllll1l11_opy_.TestFrameworkEvent(req)
                instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤ࡫ࡶࡦࡰࡷࠦᐯ"), datetime.now() - bstack1l1ll1ll1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᐰ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1ll11l1l1l1_opy_)
    def bstack1l111lll111_opy_(self, instance: bstack1llll1l1111_opy_):
        bstack1l11l11ll1l_opy_ = TestFramework.bstack1l111lll1l1_opy_(instance.context)
        for t in bstack1l11l11ll1l_opy_:
            bstack1lll111l1ll_opy_ = TestFramework.get_state(t, bstack1lll111ll1l_opy_.bstack1lll11lll11_opy_, [])
            if any(instance is d[1] for d in bstack1lll111l1ll_opy_):
                return t
    def bstack1l11l11l11l_opy_(self, message):
        self.bstack1l111llllll_opy_(message + bstack11l111_opy_ (u"ࠥࡠࡳࠨᐱ"))
    def log_error(self, message):
        self.bstack1l111lllll1_opy_(message + bstack11l111_opy_ (u"ࠦࡡࡴࠢᐲ"))
    def bstack1l11l1ll11l_opy_(self, level, original_func):
        def bstack1l11ll111l1_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack11l111_opy_ (u"ࠧࡋࡶࡦࡰࡷࡈ࡮ࡹࡰࡢࡶࡦ࡬ࡪࡸࡍࡰࡦࡸࡰࡪࠨᐳ") in message or bstack11l111_opy_ (u"ࠨ࡛ࡔࡆࡎࡇࡑࡏ࡝ࠣᐴ") in message or bstack11l111_opy_ (u"ࠢ࡜࡙ࡨࡦࡉࡸࡩࡷࡧࡵࡑࡴࡪࡵ࡭ࡧࡠࠦᐵ") in message:
                return return_value
            bstack1l11l11ll1l_opy_ = TestFramework.bstack1l11l11l111_opy_()
            if not bstack1l11l11ll1l_opy_:
                return return_value
            bstack1ll111llll1_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l11ll1l_opy_
                    if TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1lll1lll1l1_opy_)
                ),
                None,
            )
            if not bstack1ll111llll1_opy_:
                return return_value
            entry = bstack1ll11ll1l1l_opy_(TestFramework.bstack1ll1111ll11_opy_, message, level)
            self.bstack1l1llll11ll_opy_(bstack1ll111llll1_opy_, [entry])
            return return_value
        return bstack1l11ll111l1_opy_
    def bstack1l11l11l1l1_opy_(self):
        def bstack1l11l11l1ll_opy_(*args, **kwargs):
            try:
                self.bstack1l11l1ll111_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack11l111_opy_ (u"ࠨࠢࠪᐶ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack11l111_opy_ (u"ࠤࡈࡺࡪࡴࡴࡅ࡫ࡶࡴࡦࡺࡣࡩࡧࡵࡑࡴࡪࡵ࡭ࡧࠥᐷ") in message:
                    return
                bstack1l11l11ll1l_opy_ = TestFramework.bstack1l11l11l111_opy_()
                if not bstack1l11l11ll1l_opy_:
                    return
                bstack1ll111llll1_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l11ll1l_opy_
                        if TestFramework.bstack1lllllll1ll_opy_(instance, TestFramework.bstack1lll1lll1l1_opy_)
                    ),
                    None,
                )
                if not bstack1ll111llll1_opy_:
                    return
                entry = bstack1ll11ll1l1l_opy_(TestFramework.bstack1ll1111ll11_opy_, message, bstack1l11lll1l1l_opy_.bstack1l11l1111l1_opy_)
                self.bstack1l1llll11ll_opy_(bstack1ll111llll1_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l1ll111_opy_(bstack11l1ll1l_opy_ (u"ࠥ࡟ࡊࡼࡥ࡯ࡶࡇ࡭ࡸࡶࡡࡵࡥ࡫ࡩࡷࡓ࡯ࡥࡷ࡯ࡩࡢࠦࡌࡰࡩࠣࡧࡦࡶࡴࡶࡴࡨࠤࡪࡸࡲࡰࡴ࠽ࠤࢀ࡫ࡽࠣᐸ"))
                except:
                    pass
        return bstack1l11l11l1ll_opy_
    def bstack1l11l1ll1ll_opy_(self, event: dict, instance=None) -> None:
        global _1ll1l1l1l11_opy_
        levels = [bstack11l111_opy_ (u"࡙ࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢᐹ"), bstack11l111_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᐺ")]
        bstack1l11l11llll_opy_ = bstack11l111_opy_ (u"ࠨࠢᐻ")
        if instance is not None:
            try:
                bstack1l11l11llll_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1l1_opy_)
            except Exception as e:
                self.logger.warning(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡶࡷ࡬ࡨࠥ࡬ࡲࡰ࡯ࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠧᐼ").format(e))
        bstack1l11l1l1111_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᐽ")]
                bstack1ll1l1l111l_opy_ = os.path.join(bstack1ll1l1l1l1l_opy_, (bstack1ll111ll111_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1l1l111l_opy_):
                    self.logger.debug(bstack11l111_opy_ (u"ࠤࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡴ࡯ࡵࠢࡳࡶࡪࡹࡥ࡯ࡶࠣࡪࡴࡸࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡙࡫ࡳࡵࠢࡤࡲࡩࠦࡂࡶ࡫࡯ࡨࠥࡲࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡾࢁࠧᐾ").format(bstack1ll1l1l111l_opy_))
                    continue
                file_names = os.listdir(bstack1ll1l1l111l_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1l1l111l_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll1l1l1l11_opy_:
                        self.logger.info(bstack11l111_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᐿ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l1l1ll1_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l1l1ll1_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack11l111_opy_ (u"࡙ࠦ࡫ࡳࡵࡎࡨࡺࡪࡲࠢᑀ"):
                                entry = bstack1ll11ll1l1l_opy_(
                                    kind=bstack11l111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᑁ"),
                                    message=bstack11l111_opy_ (u"ࠨࠢᑂ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1llll11l1_opy_=file_size,
                                    bstack1ll1111lll1_opy_=bstack11l111_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᑃ"),
                                    bstack11ll1ll_opy_=os.path.abspath(file_path),
                                    bstack1ll111ll1_opy_=bstack1l11l11llll_opy_
                                )
                            elif level == bstack11l111_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᑄ"):
                                entry = bstack1ll11ll1l1l_opy_(
                                    kind=bstack11l111_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦᑅ"),
                                    message=bstack11l111_opy_ (u"ࠥࠦᑆ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1llll11l1_opy_=file_size,
                                    bstack1ll1111lll1_opy_=bstack11l111_opy_ (u"ࠦࡒࡇࡎࡖࡃࡏࡣ࡚ࡖࡌࡐࡃࡇࠦᑇ"),
                                    bstack11ll1ll_opy_=os.path.abspath(file_path),
                                    bstack1ll1l1ll1l1_opy_=bstack1l11l11llll_opy_
                                )
                            bstack1l11l1l1111_opy_.append(entry)
                            _1ll1l1l1l11_opy_.add(abs_path)
                        except Exception as bstack1l11l1lll11_opy_:
                            self.logger.error(bstack11l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡴࡤ࡭ࡸ࡫ࡤࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡽࢀࠦᑈ").format(bstack1l11l1lll11_opy_))
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡵࡥ࡮ࡹࡥࡥࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡾࢁࠧᑉ").format(e))
        event[bstack11l111_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᑊ")] = bstack1l11l1l1111_opy_
class bstack1l11l1l1lll_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l1ll1l1_opy_ = set()
        kwargs[bstack11l111_opy_ (u"ࠣࡵ࡮࡭ࡵࡱࡥࡺࡵࠥᑋ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l111l1l_opy_(obj, self.bstack1l11l1ll1l1_opy_)
def bstack1l11l1l11l1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l111l1l_opy_(obj, bstack1l11l1ll1l1_opy_=None, max_depth=3):
    if bstack1l11l1ll1l1_opy_ is None:
        bstack1l11l1ll1l1_opy_ = set()
    if id(obj) in bstack1l11l1ll1l1_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l1ll1l1_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l11lll1_opy_ = TestFramework.bstack1ll111111l1_opy_(obj)
    bstack1l111ll1lll_opy_ = next((k.lower() in bstack1l11l11lll1_opy_.lower() for k in bstack1l11l1lllll_opy_.keys()), None)
    if bstack1l111ll1lll_opy_:
        obj = TestFramework.bstack1ll11llll1l_opy_(obj, bstack1l11l1lllll_opy_[bstack1l111ll1lll_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11l111_opy_ (u"ࠤࡢࡣࡸࡲ࡯ࡵࡵࡢࡣࠧᑌ")):
            keys = getattr(obj, bstack11l111_opy_ (u"ࠥࡣࡤࡹ࡬ࡰࡶࡶࡣࡤࠨᑍ"), [])
        elif hasattr(obj, bstack11l111_opy_ (u"ࠦࡤࡥࡤࡪࡥࡷࡣࡤࠨᑎ")):
            keys = getattr(obj, bstack11l111_opy_ (u"ࠧࡥ࡟ࡥ࡫ࡦࡸࡤࡥࠢᑏ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11l111_opy_ (u"ࠨ࡟ࠣᑐ"))}
        if not obj and bstack1l11l11lll1_opy_ == bstack11l111_opy_ (u"ࠢࡱࡣࡷ࡬ࡱ࡯ࡢ࠯ࡒࡲࡷ࡮ࡾࡐࡢࡶ࡫ࠦᑑ"):
            obj = {bstack11l111_opy_ (u"ࠣࡲࡤࡸ࡭ࠨᑒ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l1l11l1_opy_(key) or str(key).startswith(bstack11l111_opy_ (u"ࠤࡢࠦᑓ")):
            continue
        if value is not None and bstack1l11l1l11l1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l111l1l_opy_(value, bstack1l11l1ll1l1_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l111l1l_opy_(o, bstack1l11l1ll1l1_opy_, max_depth) for o in value]))
    return result or None