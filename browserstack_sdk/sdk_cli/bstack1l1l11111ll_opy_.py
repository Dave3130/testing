# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import bstack1lllllll11l_opy_, bstack1111111111_opy_, bstack1llll1lllll_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l111_opy_ import bstack1lll11l1111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l11lll_opy_, bstack1llll111111_opy_, bstack1lll11lll11_opy_, bstack1l1lllll1ll_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll11l1lll_opy_, bstack1ll1l111111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1111l1_opy_ = [bstack1lll11l_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᏉ"), bstack1lll11l_opy_ (u"ࠧࡶࡡࡳࡧࡱࡸࠧᏊ"), bstack1lll11l_opy_ (u"ࠨࡣࡰࡰࡩ࡭࡬ࠨᏋ"), bstack1lll11l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࠣᏌ"), bstack1lll11l_opy_ (u"ࠣࡲࡤࡸ࡭ࠨᏍ")]
bstack1ll1l11lll1_opy_ = bstack1ll1l111111_opy_()
bstack1ll11ll1l1l_opy_ = bstack1lll11l_opy_ (u"ࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮ࠤᏎ")
bstack1l11l1ll1l1_opy_ = {
    bstack1lll11l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡍࡹ࡫࡭ࠣᏏ"): bstack1l11l1111l1_opy_,
    bstack1lll11l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡕࡧࡣ࡬ࡣࡪࡩࠧᏐ"): bstack1l11l1111l1_opy_,
    bstack1lll11l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡓ࡯ࡥࡷ࡯ࡩࠧᏑ"): bstack1l11l1111l1_opy_,
    bstack1lll11l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡃ࡭ࡣࡶࡷࠧᏒ"): bstack1l11l1111l1_opy_,
    bstack1lll11l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡇࡷࡱࡧࡹ࡯࡯࡯ࠤᏓ"): bstack1l11l1111l1_opy_
    + [
        bstack1lll11l_opy_ (u"ࠣࡱࡵ࡭࡬࡯࡮ࡢ࡮ࡱࡥࡲ࡫ࠢᏔ"),
        bstack1lll11l_opy_ (u"ࠤ࡮ࡩࡾࡽ࡯ࡳࡦࡶࠦᏕ"),
        bstack1lll11l_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨ࡭ࡳ࡬࡯ࠣᏖ"),
        bstack1lll11l_opy_ (u"ࠦࡰ࡫ࡹࡸࡱࡵࡨࡸࠨᏗ"),
        bstack1lll11l_opy_ (u"ࠧࡩࡡ࡭࡮ࡶࡴࡪࡩࠢᏘ"),
        bstack1lll11l_opy_ (u"ࠨࡣࡢ࡮࡯ࡳࡧࡰࠢᏙ"),
        bstack1lll11l_opy_ (u"ࠢࡴࡶࡤࡶࡹࠨᏚ"),
        bstack1lll11l_opy_ (u"ࠣࡵࡷࡳࡵࠨᏛ"),
        bstack1lll11l_opy_ (u"ࠤࡧࡹࡷࡧࡴࡪࡱࡱࠦᏜ"),
        bstack1lll11l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᏝ"),
    ],
    bstack1lll11l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡩ࡯࠰ࡖࡩࡸࡹࡩࡰࡰࠥᏞ"): [bstack1lll11l_opy_ (u"ࠧࡹࡴࡢࡴࡷࡴࡦࡺࡨࠣᏟ"), bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡷ࡫ࡧࡩ࡭ࡧࡧࠦᏠ"), bstack1lll11l_opy_ (u"ࠢࡵࡧࡶࡸࡸࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠣᏡ"), bstack1lll11l_opy_ (u"ࠣ࡫ࡷࡩࡲࡹࠢᏢ")],
    bstack1lll11l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡦࡳࡳ࡬ࡩࡨ࠰ࡆࡳࡳ࡬ࡩࡨࠤᏣ"): [bstack1lll11l_opy_ (u"ࠥ࡭ࡳࡼ࡯ࡤࡣࡷ࡭ࡴࡴ࡟ࡱࡣࡵࡥࡲࡹࠢᏤ"), bstack1lll11l_opy_ (u"ࠦࡦࡸࡧࡴࠤᏥ")],
    bstack1lll11l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡇ࡫ࡻࡸࡺࡸࡥࡅࡧࡩࠦᏦ"): [bstack1lll11l_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᏧ"), bstack1lll11l_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣᏨ"), bstack1lll11l_opy_ (u"ࠣࡨࡸࡲࡨࠨᏩ"), bstack1lll11l_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᏪ"), bstack1lll11l_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧᏫ"), bstack1lll11l_opy_ (u"ࠦ࡮ࡪࡳࠣᏬ")],
    bstack1lll11l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡔࡷࡥࡖࡪࡷࡵࡦࡵࡷࠦᏭ"): [bstack1lll11l_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦᏮ"), bstack1lll11l_opy_ (u"ࠢࡱࡣࡵࡥࡲࠨᏯ"), bstack1lll11l_opy_ (u"ࠣࡲࡤࡶࡦࡳ࡟ࡪࡰࡧࡩࡽࠨᏰ")],
    bstack1lll11l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡵࡹࡳࡴࡥࡳ࠰ࡆࡥࡱࡲࡉ࡯ࡨࡲࠦᏱ"): [bstack1lll11l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᏲ"), bstack1lll11l_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࠦᏳ")],
    bstack1lll11l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡏࡱࡧࡩࡐ࡫ࡹࡸࡱࡵࡨࡸࠨᏴ"): [bstack1lll11l_opy_ (u"ࠨ࡮ࡰࡦࡨࠦᏵ"), bstack1lll11l_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢ᏶")],
    bstack1lll11l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤࡶࡰ࠴ࡳࡵࡴࡸࡧࡹࡻࡲࡦࡵ࠱ࡑࡦࡸ࡫ࠣ᏷"): [bstack1lll11l_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᏸ"), bstack1lll11l_opy_ (u"ࠥࡥࡷ࡭ࡳࠣᏹ"), bstack1lll11l_opy_ (u"ࠦࡰࡽࡡࡳࡩࡶࠦᏺ")],
}
_1ll111l1111_opy_ = set()
class bstack1l1l1llll11_opy_(bstack1lllllll1l1_opy_):
    bstack1l111ll1ll1_opy_ = bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡪ࡬ࡥࡳࡴࡨࡨࠧᏻ")
    bstack1l11l11l1l1_opy_ = bstack1lll11l_opy_ (u"ࠨࡉࡏࡈࡒࠦᏼ")
    bstack1l11l1ll111_opy_ = bstack1lll11l_opy_ (u"ࠢࡆࡔࡕࡓࡗࠨᏽ")
    bstack1l11l1ll11l_opy_: Callable
    bstack1l11l1lll1l_opy_: Callable
    def __init__(self, bstack1l1l1l11l11_opy_, bstack1ll1lll111l_opy_):
        super().__init__()
        self.bstack1l11l11l111_opy_ = bstack1ll1lll111l_opy_
        if os.getenv(bstack1lll11l_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡐ࠳࠴࡝ࠧ᏾"), bstack1lll11l_opy_ (u"ࠤ࠴ࠦ᏿")) != bstack1lll11l_opy_ (u"ࠥ࠵ࠧ᐀") or not self.is_enabled():
            self.logger.warning(bstack1lll11l_opy_ (u"ࠦࠧᐁ") + str(self.__class__.__name__) + bstack1lll11l_opy_ (u"ࠧࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠣᐂ"))
            return
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.PRE), self.bstack1llll111l11_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.POST), self.bstack1lll1lll1ll_opy_)
        for event in bstack1lll1l11lll_opy_:
            for state in bstack1lll11lll11_opy_:
                TestFramework.bstack1lllll11111_opy_((event, state), self.bstack1l11l11ll11_opy_)
        bstack1l1l1l11l11_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.POST), self.bstack1l11l11ll1l_opy_)
        self.bstack1l11l1ll11l_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l1l11l1_opy_(bstack1l1l1llll11_opy_.bstack1l11l11l1l1_opy_, self.bstack1l11l1ll11l_opy_)
        self.bstack1l11l1lll1l_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l1l11l1_opy_(bstack1l1l1llll11_opy_.bstack1l11l1ll111_opy_, self.bstack1l11l1lll1l_opy_)
        self.bstack1l111lllll1_opy_ = builtins.print
        builtins.print = self.bstack1l11l1l1l11_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll1111ll1l_opy_() and instance:
            bstack1l111ll1l1l_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllll1l111_opy_
            if test_framework_state == bstack1lll1l11lll_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1l11lll_opy_.LOG:
                bstack11ll11l1l_opy_ = datetime.now()
                entries = f.bstack1ll1l11l11l_opy_(instance, bstack1lllll1l111_opy_)
                if entries:
                    self.bstack1ll1l11l1l1_opy_(instance, entries)
                    instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࠨᐃ"), datetime.now() - bstack11ll11l1l_opy_)
                    f.bstack1ll11l11l11_opy_(instance, bstack1lllll1l111_opy_)
                instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᐄ"), datetime.now() - bstack1l111ll1l1l_opy_)
                return # do not send this event with the bstack1l11l1lllll_opy_ bstack1l11l11lll1_opy_
            elif (
                test_framework_state == bstack1lll1l11lll_opy_.TEST
                and test_hook_state == bstack1lll11lll11_opy_.POST
                and not f.bstack1llll11ll11_opy_(instance, TestFramework.bstack1ll1l11ll11_opy_)
            ):
                self.logger.warning(bstack1lll11l_opy_ (u"ࠣࡦࡵࡳࡵࡶࡩ࡯ࡩࠣࡨࡺ࡫ࠠࡵࡱࠣࡰࡦࡩ࡫ࠡࡱࡩࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࠨᐅ") + str(TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1ll1l11ll11_opy_)) + bstack1lll11l_opy_ (u"ࠤࠥᐆ"))
                f.bstack1llll1ll11l_opy_(instance, bstack1l1l1llll11_opy_.bstack1l111ll1ll1_opy_, True)
                return # do not send this event bstack1l111llllll_opy_ bstack1l111lll1ll_opy_
            elif (
                f.get_state(instance, bstack1l1l1llll11_opy_.bstack1l111ll1ll1_opy_, False)
                and test_framework_state == bstack1lll1l11lll_opy_.LOG_REPORT
                and test_hook_state == bstack1lll11lll11_opy_.POST
                and f.bstack1llll11ll11_opy_(instance, TestFramework.bstack1ll1l11ll11_opy_)
            ):
                self.logger.warning(bstack1lll11l_opy_ (u"ࠥ࡭ࡳࡰࡥࡤࡶ࡬ࡲ࡬ࠦࡔࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲࡙ࡋࡓࡕ࠮ࠣࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡔࡔ࡙ࡔࠡࠤᐇ") + str(TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1ll1l11ll11_opy_)) + bstack1lll11l_opy_ (u"ࠦࠧᐈ"))
                self.bstack1l11l11ll11_opy_(f, instance, (bstack1lll1l11lll_opy_.TEST, bstack1lll11lll11_opy_.POST), *args, **kwargs)
            bstack11ll11l1l_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11ll1111l_opy_ = sorted(
                filter(lambda x: x.get(bstack1lll11l_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᐉ"), None), data.pop(bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᐊ"), {}).values()),
                key=lambda x: x[bstack1lll11l_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᐋ")],
            )
            if bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_ in data:
                data.pop(bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_)
            data.update({bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᐌ"): bstack1l11ll1111l_opy_})
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᐍ"), datetime.now() - bstack11ll11l1l_opy_)
            bstack11ll11l1l_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l111ll1_opy_)
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠥ࡮ࡸࡵ࡮࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨᐎ"), datetime.now() - bstack11ll11l1l_opy_)
            self.bstack1l11l11lll1_opy_(instance, bstack1lllll1l111_opy_, event_json=event_json)
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᐏ"), datetime.now() - bstack1l111ll1l1l_opy_)
    def bstack1llll111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
        bstack1ll111111l1_opy_ = bstack1llll1l1l1l_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack1l1l11ll11_opy_.value)
        self.bstack1l11l11l111_opy_.bstack1llll11l111_opy_(instance, f, bstack1lllll1l111_opy_, *args, **kwargs)
        bstack1llll1l1l1l_opy_.end(EVENTS.bstack1l1l11ll11_opy_.value, bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᐐ"), bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᐑ"), status=True, failure=None, test_name=None)
    def bstack1lll1lll1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l11l111_opy_.bstack1lll11ll111_opy_(instance, f, bstack1lllll1l111_opy_, *args, **kwargs)
        self.bstack1l111lll111_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11ll11111_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1l111lll111_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll111111_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡗࡩࡸࡺࡓࡦࡵࡶ࡭ࡴࡴࡅࡷࡧࡱࡸࠥ࡭ࡒࡑࡅࠣࡧࡦࡲ࡬࠻ࠢࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡪࡡࡵࡣࠥᐒ"))
            return
        bstack11ll11l1l_opy_ = datetime.now()
        try:
            r = self.bstack1llll11l11l_opy_.TestSessionEvent(req)
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡩࡻ࡫࡮ࡵࠤᐓ"), datetime.now() - bstack11ll11l1l_opy_)
            f.bstack1llll1ll11l_opy_(instance, self.bstack1l11l11l111_opy_.bstack1lll11l1ll1_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1lll11l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᐔ") + str(r) + bstack1lll11l_opy_ (u"ࠥࠦᐕ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᐖ") + str(e) + bstack1lll11l_opy_ (u"ࠧࠨᐗ"))
            traceback.print_exc()
            raise e
    def bstack1l11l11ll1l_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        _driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        _1l11l11llll_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1llllll1ll1_opy_.bstack1l1lll1111l_opy_(method_name):
            return
        if f.bstack1l1ll1ll1l1_opy_(*args) == bstack1llllll1ll1_opy_.bstack1l11l11111l_opy_:
            bstack1l111ll1l1l_opy_ = datetime.now()
            screenshot = result.get(bstack1lll11l_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧᐘ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1lll11l_opy_ (u"ࠢࡪࡰࡹࡥࡱ࡯ࡤࠡࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠥ࡯࡭ࡢࡩࡨࠤࡧࡧࡳࡦ࠸࠷ࠤࡸࡺࡲࠣᐙ"))
                return
            bstack1ll1l11llll_opy_ = self.bstack1l111lll1l1_opy_(instance)
            if bstack1ll1l11llll_opy_:
                entry = bstack1l1lllll1ll_opy_(TestFramework.bstack1l11l1ll1ll_opy_, screenshot)
                self.bstack1ll1l11l1l1_opy_(bstack1ll1l11llll_opy_, [entry])
                instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡧࡻࡩࡨࡻࡴࡦࠤᐚ"), datetime.now() - bstack1l111ll1l1l_opy_)
            else:
                self.logger.warning(bstack1lll11l_opy_ (u"ࠤࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡶࡨࡷࡹࠦࡦࡰࡴࠣࡻ࡭࡯ࡣࡩࠢࡷ࡬࡮ࡹࠠࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠤࡼࡧࡳࠡࡶࡤ࡯ࡪࡴࠠࡣࡻࠣࡨࡷ࡯ࡶࡦࡴࡀࠤࢀࢃࠢᐛ").format(instance.ref()))
        event = {}
        bstack1ll1l11llll_opy_ = self.bstack1l111lll1l1_opy_(instance)
        if bstack1ll1l11llll_opy_:
            self.bstack1l11l111111_opy_(event, bstack1ll1l11llll_opy_)
            if event.get(bstack1lll11l_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᐜ")):
                self.bstack1ll1l11l1l1_opy_(bstack1ll1l11llll_opy_, event[bstack1lll11l_opy_ (u"ࠦࡱࡵࡧࡴࠤᐝ")])
            else:
                self.logger.debug(bstack1lll11l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡱࡵࡧࡴࠢࡩࡳࡷࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡩࡻ࡫࡮ࡵࠤᐞ"))
    @measure(event_name=EVENTS.bstack1l11l1l111l_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1ll1l11l1l1_opy_(
        self,
        bstack1ll1l11llll_opy_: bstack1llll111111_opy_,
        entries: List[bstack1l1lllll1ll_opy_],
    ):
        self.bstack1llllll1lll_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1lllllllll1_opy_)
        req.execution_context.hash = str(bstack1ll1l11llll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1l11llll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1l11llll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1lll1l1l111_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll1l11llll_opy_, TestFramework.bstack1lll11ll11l_opy_)
            log_entry.test_framework_state = bstack1ll1l11llll_opy_.state.name
            log_entry.message = entry.message.encode(bstack1lll11l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᐟ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1lll11l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᐠ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11111l1l_opy_
                log_entry.file_path = entry.bstack1ll111l_opy_
        def bstack1l1llll1l11_opy_():
            bstack11ll11l1l_opy_ = datetime.now()
            try:
                self.bstack1llll11l11l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l1ll1ll_opy_:
                    bstack1ll1l11llll_opy_.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᐡ"), datetime.now() - bstack11ll11l1l_opy_)
                elif entry.kind == TestFramework.bstack1l111llll11_opy_:
                    bstack1ll1l11llll_opy_.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨᐢ"), datetime.now() - bstack11ll11l1l_opy_)
                else:
                    bstack1ll1l11llll_opy_.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡰࡴ࡭ࠢᐣ"), datetime.now() - bstack11ll11l1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lll11l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᐤ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1l1llll1l11_opy_)
    @measure(event_name=EVENTS.bstack1l11l11l1ll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1l11l11lll1_opy_(
        self,
        instance: bstack1llll111111_opy_,
        bstack1lllll1l111_opy_: Tuple[bstack1lll1l11lll_opy_, bstack1lll11lll11_opy_],
        event_json=None,
    ):
        self.bstack1llllll1lll_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllllllll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l1l111_opy_)
        req.test_framework_state = bstack1lllll1l111_opy_[0].name
        req.test_hook_state = bstack1lllll1l111_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1l1lllll111_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll111ll1ll_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l111ll1_opy_)).encode(bstack1lll11l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᐥ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1l1llll1l11_opy_():
            bstack11ll11l1l_opy_ = datetime.now()
            try:
                self.bstack1llll11l11l_opy_.TestFrameworkEvent(req)
                instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡩࡻ࡫࡮ࡵࠤᐦ"), datetime.now() - bstack11ll11l1l_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1lll11l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᐧ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1l1l_opy_.enqueue(bstack1l1llll1l11_opy_)
    def bstack1l111lll1l1_opy_(self, instance: bstack1lllllll11l_opy_):
        bstack1l111lll11l_opy_ = TestFramework.bstack1l11l1l1111_opy_(instance.context)
        for t in bstack1l111lll11l_opy_:
            bstack1lll111l1l1_opy_ = TestFramework.get_state(t, bstack1lll11l1111_opy_.bstack1lll11ll1l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll111l1l1_opy_):
                return t
    def bstack1l11l1111ll_opy_(self, message):
        self.bstack1l11l1ll11l_opy_(message + bstack1lll11l_opy_ (u"ࠣ࡞ࡱࠦᐨ"))
    def log_error(self, message):
        self.bstack1l11l1lll1l_opy_(message + bstack1lll11l_opy_ (u"ࠤ࡟ࡲࠧᐩ"))
    def bstack1l11l1l11l1_opy_(self, level, original_func):
        def bstack1l11l1l1lll_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1lll11l_opy_ (u"ࠥࡉࡻ࡫࡮ࡵࡆ࡬ࡷࡵࡧࡴࡤࡪࡨࡶࡒࡵࡤࡶ࡮ࡨࠦᐪ") in message or bstack1lll11l_opy_ (u"ࠦࡠ࡙ࡄࡌࡅࡏࡍࡢࠨᐫ") in message or bstack1lll11l_opy_ (u"ࠧࡡࡗࡦࡤࡇࡶ࡮ࡼࡥࡳࡏࡲࡨࡺࡲࡥ࡞ࠤᐬ") in message:
                return return_value
            bstack1l111lll11l_opy_ = TestFramework.bstack1l11l111l1l_opy_()
            if not bstack1l111lll11l_opy_:
                return return_value
            bstack1ll1l11llll_opy_ = next(
                (
                    instance
                    for instance in bstack1l111lll11l_opy_
                    if TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1lll11ll11l_opy_)
                ),
                None,
            )
            if not bstack1ll1l11llll_opy_:
                return return_value
            entry = bstack1l1lllll1ll_opy_(TestFramework.bstack1l1lllll1l1_opy_, message, level)
            self.bstack1ll1l11l1l1_opy_(bstack1ll1l11llll_opy_, [entry])
            return return_value
        return bstack1l11l1l1lll_opy_
    def bstack1l11l1l1l11_opy_(self):
        def bstack1l11l111l11_opy_(*args, **kwargs):
            try:
                self.bstack1l111lllll1_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1lll11l_opy_ (u"࠭ࠠࠨᐭ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1lll11l_opy_ (u"ࠢࡆࡸࡨࡲࡹࡊࡩࡴࡲࡤࡸࡨ࡮ࡥࡳࡏࡲࡨࡺࡲࡥࠣᐮ") in message:
                    return
                bstack1l111lll11l_opy_ = TestFramework.bstack1l11l111l1l_opy_()
                if not bstack1l111lll11l_opy_:
                    return
                bstack1ll1l11llll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l111lll11l_opy_
                        if TestFramework.bstack1llll11ll11_opy_(instance, TestFramework.bstack1lll11ll11l_opy_)
                    ),
                    None,
                )
                if not bstack1ll1l11llll_opy_:
                    return
                entry = bstack1l1lllll1ll_opy_(TestFramework.bstack1l1lllll1l1_opy_, message, bstack1l1l1llll11_opy_.bstack1l11l11l1l1_opy_)
                self.bstack1ll1l11l1l1_opy_(bstack1ll1l11llll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l111lllll1_opy_(bstack1lll1ll1l11_opy_ (u"ࠣ࡝ࡈࡺࡪࡴࡴࡅ࡫ࡶࡴࡦࡺࡣࡩࡧࡵࡑࡴࡪࡵ࡭ࡧࡠࠤࡑࡵࡧࠡࡥࡤࡴࡹࡻࡲࡦࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࡩࢂࠨᐯ"))
                except:
                    pass
        return bstack1l11l111l11_opy_
    def bstack1l11l111111_opy_(self, event: dict, instance=None) -> None:
        global _1ll111l1111_opy_
        levels = [bstack1lll11l_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᐰ"), bstack1lll11l_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᐱ")]
        bstack1l111llll1l_opy_ = bstack1lll11l_opy_ (u"ࠦࠧᐲ")
        if instance is not None:
            try:
                bstack1l111llll1l_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll11ll11l_opy_)
            except Exception as e:
                self.logger.warning(bstack1lll11l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡻࡵࡪࡦࠣࡪࡷࡵ࡭ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠥᐳ").format(e))
        bstack1l11l1l1l1l_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᐴ")]
                bstack1ll11lllll1_opy_ = os.path.join(bstack1ll1l11lll1_opy_, (bstack1ll11ll1l1l_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll11lllll1_opy_):
                    self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡲࡴࡺࠠࡱࡴࡨࡷࡪࡴࡴࠡࡨࡲࡶࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡗࡩࡸࡺࠠࡢࡰࡧࠤࡇࡻࡩ࡭ࡦࠣࡰࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡼࡿࠥᐵ").format(bstack1ll11lllll1_opy_))
                    continue
                file_names = os.listdir(bstack1ll11lllll1_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll11lllll1_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll111l1111_opy_:
                        self.logger.info(bstack1lll11l_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᐶ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l11l11l_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l11l11l_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1lll11l_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᐷ"):
                                entry = bstack1l1lllll1ll_opy_(
                                    kind=bstack1lll11l_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐸ"),
                                    message=bstack1lll11l_opy_ (u"ࠦࠧᐹ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11111l1l_opy_=file_size,
                                    bstack1ll1l1l111l_opy_=bstack1lll11l_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧᐺ"),
                                    bstack1ll111l_opy_=os.path.abspath(file_path),
                                    bstack1111ll111_opy_=bstack1l111llll1l_opy_
                                )
                            elif level == bstack1lll11l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᐻ"):
                                entry = bstack1l1lllll1ll_opy_(
                                    kind=bstack1lll11l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᐼ"),
                                    message=bstack1lll11l_opy_ (u"ࠣࠤᐽ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11111l1l_opy_=file_size,
                                    bstack1ll1l1l111l_opy_=bstack1lll11l_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᐾ"),
                                    bstack1ll111l_opy_=os.path.abspath(file_path),
                                    bstack1ll1l1l1lll_opy_=bstack1l111llll1l_opy_
                                )
                            bstack1l11l1l1l1l_opy_.append(entry)
                            _1ll111l1111_opy_.add(abs_path)
                        except Exception as bstack1l11l1lll11_opy_:
                            self.logger.error(bstack1lll11l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡲࡢ࡫ࡶࡩࡩࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤᐿ").format(bstack1l11l1lll11_opy_))
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡳࡣ࡬ࡷࡪࡪࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡼࡿࠥᑀ").format(e))
        event[bstack1lll11l_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᑁ")] = bstack1l11l1l1l1l_opy_
class bstack1l11l111ll1_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l1l1ll1_opy_ = set()
        kwargs[bstack1lll11l_opy_ (u"ࠨࡳ࡬࡫ࡳ࡯ࡪࡿࡳࠣᑂ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l111lll_opy_(obj, self.bstack1l11l1l1ll1_opy_)
def bstack1l11l1llll1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l111lll_opy_(obj, bstack1l11l1l1ll1_opy_=None, max_depth=3):
    if bstack1l11l1l1ll1_opy_ is None:
        bstack1l11l1l1ll1_opy_ = set()
    if id(obj) in bstack1l11l1l1ll1_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l1l1ll1_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l111ll1lll_opy_ = TestFramework.bstack1ll1111l1ll_opy_(obj)
    bstack1l11l1l11ll_opy_ = next((k.lower() in bstack1l111ll1lll_opy_.lower() for k in bstack1l11l1ll1l1_opy_.keys()), None)
    if bstack1l11l1l11ll_opy_:
        obj = TestFramework.bstack1l1llll1ll1_opy_(obj, bstack1l11l1ll1l1_opy_[bstack1l11l1l11ll_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1lll11l_opy_ (u"ࠢࡠࡡࡶࡰࡴࡺࡳࡠࡡࠥᑃ")):
            keys = getattr(obj, bstack1lll11l_opy_ (u"ࠣࡡࡢࡷࡱࡵࡴࡴࡡࡢࠦᑄ"), [])
        elif hasattr(obj, bstack1lll11l_opy_ (u"ࠤࡢࡣࡩ࡯ࡣࡵࡡࡢࠦᑅ")):
            keys = getattr(obj, bstack1lll11l_opy_ (u"ࠥࡣࡤࡪࡩࡤࡶࡢࡣࠧᑆ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1lll11l_opy_ (u"ࠦࡤࠨᑇ"))}
        if not obj and bstack1l111ll1lll_opy_ == bstack1lll11l_opy_ (u"ࠧࡶࡡࡵࡪ࡯࡭ࡧ࠴ࡐࡰࡵ࡬ࡼࡕࡧࡴࡩࠤᑈ"):
            obj = {bstack1lll11l_opy_ (u"ࠨࡰࡢࡶ࡫ࠦᑉ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l1llll1_opy_(key) or str(key).startswith(bstack1lll11l_opy_ (u"ࠢࡠࠤᑊ")):
            continue
        if value is not None and bstack1l11l1llll1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l111lll_opy_(value, bstack1l11l1l1ll1_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l111lll_opy_(o, bstack1l11l1l1ll1_opy_, max_depth) for o in value]))
    return result or None