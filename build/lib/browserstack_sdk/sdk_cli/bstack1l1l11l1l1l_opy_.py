# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1lllll111l1_opy_ import bstack1llll1ll11l_opy_, bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll111l1l_opy_ import bstack1llll1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1111ll1_opy_ import bstack1lll1111l11_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll1ll1_opy_, bstack1lll1ll11ll_opy_, bstack1lll11l11ll_opy_, bstack1l1lllll11l_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1lllll1_opy_, bstack1ll1l11llll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1111ll_opy_ = [bstack11l1111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᏣ"), bstack11l1111_opy_ (u"ࠥࡴࡦࡸࡥ࡯ࡶࠥᏤ"), bstack11l1111_opy_ (u"ࠦࡨࡵ࡮ࡧ࡫ࡪࠦᏥ"), bstack11l1111_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࠨᏦ"), bstack11l1111_opy_ (u"ࠨࡰࡢࡶ࡫ࠦᏧ")]
bstack1ll1111111l_opy_ = bstack1ll1l11llll_opy_()
bstack1l1llllllll_opy_ = bstack11l1111_opy_ (u"ࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢᏨ")
bstack1l111lll1ll_opy_ = {
    bstack11l1111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡋࡷࡩࡲࠨᏩ"): bstack1l11l1111ll_opy_,
    bstack11l1111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡓࡥࡨࡱࡡࡨࡧࠥᏪ"): bstack1l11l1111ll_opy_,
    bstack11l1111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡑࡴࡪࡵ࡭ࡧࠥᏫ"): bstack1l11l1111ll_opy_,
    bstack11l1111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡈࡲࡡࡴࡵࠥᏬ"): bstack1l11l1111ll_opy_,
    bstack11l1111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡌࡵ࡯ࡥࡷ࡭ࡴࡴࠢᏭ"): bstack1l11l1111ll_opy_
    + [
        bstack11l1111_opy_ (u"ࠨ࡯ࡳ࡫ࡪ࡭ࡳࡧ࡬࡯ࡣࡰࡩࠧᏮ"),
        bstack11l1111_opy_ (u"ࠢ࡬ࡧࡼࡻࡴࡸࡤࡴࠤᏯ"),
        bstack11l1111_opy_ (u"ࠣࡨ࡬ࡼࡹࡻࡲࡦ࡫ࡱࡪࡴࠨᏰ"),
        bstack11l1111_opy_ (u"ࠤ࡮ࡩࡾࡽ࡯ࡳࡦࡶࠦᏱ"),
        bstack11l1111_opy_ (u"ࠥࡧࡦࡲ࡬ࡴࡲࡨࡧࠧᏲ"),
        bstack11l1111_opy_ (u"ࠦࡨࡧ࡬࡭ࡱࡥ࡮ࠧᏳ"),
        bstack11l1111_opy_ (u"ࠧࡹࡴࡢࡴࡷࠦᏴ"),
        bstack11l1111_opy_ (u"ࠨࡳࡵࡱࡳࠦᏵ"),
        bstack11l1111_opy_ (u"ࠢࡥࡷࡵࡥࡹ࡯࡯࡯ࠤ᏶"),
        bstack11l1111_opy_ (u"ࠣࡹ࡫ࡩࡳࠨ᏷"),
    ],
    bstack11l1111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡰࡥ࡮ࡴ࠮ࡔࡧࡶࡷ࡮ࡵ࡮ࠣᏸ"): [bstack11l1111_opy_ (u"ࠥࡷࡹࡧࡲࡵࡲࡤࡸ࡭ࠨᏹ"), bstack11l1111_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࡩࡥ࡮ࡲࡥࡥࠤᏺ"), bstack11l1111_opy_ (u"ࠧࡺࡥࡴࡶࡶࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࠨᏻ"), bstack11l1111_opy_ (u"ࠨࡩࡵࡧࡰࡷࠧᏼ")],
    bstack11l1111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡤࡱࡱࡪ࡮࡭࠮ࡄࡱࡱࡪ࡮࡭ࠢᏽ"): [bstack11l1111_opy_ (u"ࠣ࡫ࡱࡺࡴࡩࡡࡵ࡫ࡲࡲࡤࡶࡡࡳࡣࡰࡷࠧ᏾"), bstack11l1111_opy_ (u"ࠤࡤࡶ࡬ࡹࠢ᏿")],
    bstack11l1111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡪ࡮ࡾࡴࡶࡴࡨࡷ࠳ࡌࡩࡹࡶࡸࡶࡪࡊࡥࡧࠤ᐀"): [bstack11l1111_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᐁ"), bstack11l1111_opy_ (u"ࠧࡧࡲࡨࡰࡤࡱࡪࠨᐂ"), bstack11l1111_opy_ (u"ࠨࡦࡶࡰࡦࠦᐃ"), bstack11l1111_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢᐄ"), bstack11l1111_opy_ (u"ࠣࡷࡱ࡭ࡹࡺࡥࡴࡶࠥᐅ"), bstack11l1111_opy_ (u"ࠤ࡬ࡨࡸࠨᐆ")],
    bstack11l1111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡪ࡮ࡾࡴࡶࡴࡨࡷ࠳࡙ࡵࡣࡔࡨࡵࡺ࡫ࡳࡵࠤᐇ"): [bstack11l1111_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦࠤᐈ"), bstack11l1111_opy_ (u"ࠧࡶࡡࡳࡣࡰࠦᐉ"), bstack11l1111_opy_ (u"ࠨࡰࡢࡴࡤࡱࡤ࡯࡮ࡥࡧࡻࠦᐊ")],
    bstack11l1111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡳࡷࡱࡲࡪࡸ࠮ࡄࡣ࡯ࡰࡎࡴࡦࡰࠤᐋ"): [bstack11l1111_opy_ (u"ࠣࡹ࡫ࡩࡳࠨᐌ"), bstack11l1111_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࠤᐍ")],
    bstack11l1111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡱࡦࡸ࡫࠯ࡵࡷࡶࡺࡩࡴࡶࡴࡨࡷ࠳ࡔ࡯ࡥࡧࡎࡩࡾࡽ࡯ࡳࡦࡶࠦᐎ"): [bstack11l1111_opy_ (u"ࠦࡳࡵࡤࡦࠤᐏ"), bstack11l1111_opy_ (u"ࠧࡶࡡࡳࡧࡱࡸࠧᐐ")],
    bstack11l1111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴࡭ࡢࡴ࡮࠲ࡸࡺࡲࡶࡥࡷࡹࡷ࡫ࡳ࠯ࡏࡤࡶࡰࠨᐑ"): [bstack11l1111_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᐒ"), bstack11l1111_opy_ (u"ࠣࡣࡵ࡫ࡸࠨᐓ"), bstack11l1111_opy_ (u"ࠤ࡮ࡻࡦࡸࡧࡴࠤᐔ")],
}
_1ll11l1l111_opy_ = set()
class bstack1l1l11ll111_opy_(bstack1llll1l1ll1_opy_):
    bstack1l111llllll_opy_ = bstack11l1111_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡨࡪࡪࡸࡲࡦࡦࠥᐕ")
    bstack1l11l111l1l_opy_ = bstack11l1111_opy_ (u"ࠦࡎࡔࡆࡐࠤᐖ")
    bstack1l11l11111l_opy_ = bstack11l1111_opy_ (u"ࠧࡋࡒࡓࡑࡕࠦᐗ")
    bstack1l11l11llll_opy_: Callable
    bstack1l11l111lll_opy_: Callable
    def __init__(self, bstack1l1l111111l_opy_, bstack1ll1ll11lll_opy_):
        super().__init__()
        self.bstack1l11l1l111l_opy_ = bstack1ll1ll11lll_opy_
        if os.getenv(bstack11l1111_opy_ (u"ࠨࡓࡅࡍࡢࡇࡑࡏ࡟ࡇࡎࡄࡋࡤࡕ࠱࠲࡛ࠥᐘ"), bstack11l1111_opy_ (u"ࠢ࠲ࠤᐙ")) != bstack11l1111_opy_ (u"ࠣ࠳ࠥᐚ") or not self.is_enabled():
            self.logger.warning(bstack11l1111_opy_ (u"ࠤࠥᐛ") + str(self.__class__.__name__) + bstack11l1111_opy_ (u"ࠥࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩࠨᐜ"))
            return
        TestFramework.bstack1llllll11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll11l11ll_opy_.PRE), self.bstack1lll1l1l11l_opy_)
        TestFramework.bstack1llllll11l1_opy_((bstack1lll1ll1ll1_opy_.TEST, bstack1lll11l11ll_opy_.POST), self.bstack1lll1l1l111_opy_)
        for event in bstack1lll1ll1ll1_opy_:
            for state in bstack1lll11l11ll_opy_:
                TestFramework.bstack1llllll11l1_opy_((event, state), self.bstack1l11l11l111_opy_)
        bstack1l1l111111l_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.bstack1llll1l1l1l_opy_, bstack1lllll11ll1_opy_.POST), self.bstack1l11l11ll11_opy_)
        self.bstack1l11l11llll_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11l111l11_opy_(bstack1l1l11ll111_opy_.bstack1l11l111l1l_opy_, self.bstack1l11l11llll_opy_)
        self.bstack1l11l111lll_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11l111l11_opy_(bstack1l1l11ll111_opy_.bstack1l11l11111l_opy_, self.bstack1l11l111lll_opy_)
        self.bstack1l11l1l1l11_opy_ = builtins.print
        builtins.print = self.bstack1l11l11lll1_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll11ll11ll_opy_() and instance:
            bstack1l111ll1lll_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1llllll1lll_opy_
            if test_framework_state == bstack1lll1ll1ll1_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1ll1ll1_opy_.LOG:
                bstack11ll111l1_opy_ = datetime.now()
                entries = f.bstack1ll1l111lll_opy_(instance, bstack1llllll1lll_opy_)
                if entries:
                    self.bstack1l1lll1ll1l_opy_(instance, entries)
                    instance.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟࡭ࡱࡪࡣࡨࡸࡥࡢࡶࡨࡨࡤ࡫ࡶࡦࡰࡷࠦᐝ"), datetime.now() - bstack11ll111l1_opy_)
                    f.bstack1ll11111ll1_opy_(instance, bstack1llllll1lll_opy_)
                instance.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠧࡵ࠱࠲ࡻ࠽ࡳࡳࡥࡡ࡭࡮ࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺࡳࠣᐞ"), datetime.now() - bstack1l111ll1lll_opy_)
                return # do not send this event with the bstack1l11l11l1ll_opy_ bstack1l111lll1l1_opy_
            elif (
                test_framework_state == bstack1lll1ll1ll1_opy_.TEST
                and test_hook_state == bstack1lll11l11ll_opy_.POST
                and not f.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll1l11l1l1_opy_)
            ):
                self.logger.warning(bstack11l1111_opy_ (u"ࠨࡤࡳࡱࡳࡴ࡮ࡴࡧࠡࡦࡸࡩࠥࡺ࡯ࠡ࡮ࡤࡧࡰࠦ࡯ࡧࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࠦᐟ") + str(TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll1l11l1l1_opy_)) + bstack11l1111_opy_ (u"ࠢࠣᐠ"))
                f.bstack1llllll1111_opy_(instance, bstack1l1l11ll111_opy_.bstack1l111llllll_opy_, True)
                return # do not send this event bstack1l11l111ll1_opy_ bstack1l11l1l11ll_opy_
            elif (
                f.get_state(instance, bstack1l1l11ll111_opy_.bstack1l111llllll_opy_, False)
                and test_framework_state == bstack1lll1ll1ll1_opy_.LOG_REPORT
                and test_hook_state == bstack1lll11l11ll_opy_.POST
                and f.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll1l11l1l1_opy_)
            ):
                self.logger.warning(bstack11l1111_opy_ (u"ࠣ࡫ࡱ࡮ࡪࡩࡴࡪࡰࡪࠤ࡙࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡗࡹࡧࡴࡦ࠰ࡗࡉࡘ࡚ࠬࠡࡖࡨࡷࡹࡎ࡯ࡰ࡭ࡖࡸࡦࡺࡥ࠯ࡒࡒࡗ࡙ࠦࠢᐡ") + str(TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll1l11l1l1_opy_)) + bstack11l1111_opy_ (u"ࠤࠥᐢ"))
                self.bstack1l11l11l111_opy_(f, instance, (bstack1lll1ll1ll1_opy_.TEST, bstack1lll11l11ll_opy_.POST), *args, **kwargs)
            bstack11ll111l1_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l1111l1_opy_ = sorted(
                filter(lambda x: x.get(bstack11l1111_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᐣ"), None), data.pop(bstack11l1111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᐤ"), {}).values()),
                key=lambda x: x[bstack11l1111_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᐥ")],
            )
            if bstack1lll1111l11_opy_.bstack1llll111111_opy_ in data:
                data.pop(bstack1lll1111l11_opy_.bstack1llll111111_opy_)
            data.update({bstack11l1111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᐦ"): bstack1l11l1111l1_opy_})
            instance.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠢ࡫ࡵࡲࡲ࠿ࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᐧ"), datetime.now() - bstack11ll111l1_opy_)
            bstack11ll111l1_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l111ll1ll1_opy_)
            instance.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠣ࡬ࡶࡳࡳࡀ࡯࡯ࡡࡤࡰࡱࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶࡶࠦᐨ"), datetime.now() - bstack11ll111l1_opy_)
            self.bstack1l111lll1l1_opy_(instance, bstack1llllll1lll_opy_, event_json=event_json)
            instance.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠤࡲ࠵࠶ࡿ࠺ࡰࡰࡢࡥࡱࡲ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷࡷࠧᐩ"), datetime.now() - bstack1l111ll1lll_opy_)
    def bstack1lll1l1l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111111l1l1_opy_ import bstack1llll1l1111_opy_
        bstack1l1llll111l_opy_ = bstack1llll1l1111_opy_.bstack1ll1111l111_opy_(EVENTS.bstack1l11ll11ll_opy_.value)
        self.bstack1l11l1l111l_opy_.bstack1lll11lllll_opy_(instance, f, bstack1llllll1lll_opy_, *args, **kwargs)
        bstack1llll1l1111_opy_.end(EVENTS.bstack1l11ll11ll_opy_.value, bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᐪ"), bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᐫ"), status=True, failure=None, test_name=None)
    def bstack1lll1l1l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11l1l111l_opy_.bstack1lll11ll1ll_opy_(instance, f, bstack1llllll1lll_opy_, *args, **kwargs)
        self.bstack1l111ll111l_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l111ll1l11_opy_, stage=STAGE.bstack1111ll111_opy_)
    def bstack1l111ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll11ll_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack11l1111_opy_ (u"࡙ࠧ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡕࡧࡶࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡊࡼࡥ࡯ࡶࠣ࡫ࡗࡖࡃࠡࡥࡤࡰࡱࡀࠠࡏࡱࠣࡺࡦࡲࡩࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡨࡦࡺࡡࠣᐬ"))
            return
        bstack11ll111l1_opy_ = datetime.now()
        try:
            r = self.bstack1llll1l1lll_opy_.TestSessionEvent(req)
            instance.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡧࡹࡩࡳࡺࠢᐭ"), datetime.now() - bstack11ll111l1_opy_)
            f.bstack1llllll1111_opy_(instance, self.bstack1l11l1l111l_opy_.bstack1lll11ll1l1_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11l1111_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᐮ") + str(r) + bstack11l1111_opy_ (u"ࠣࠤᐯ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᐰ") + str(e) + bstack11l1111_opy_ (u"ࠥࠦᐱ"))
            traceback.print_exc()
            raise e
    def bstack1l11l11ll11_opy_(
        self,
        f: bstack1lllll11111_opy_,
        _driver: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        _1l111llll1l_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllll11111_opy_.bstack1l1ll1l11l1_opy_(method_name):
            return
        if f.bstack1l1ll1ll1ll_opy_(*args) == bstack1lllll11111_opy_.bstack1l111lll11l_opy_:
            bstack1l111ll1lll_opy_ = datetime.now()
            screenshot = result.get(bstack11l1111_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥᐲ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack11l1111_opy_ (u"ࠧ࡯࡮ࡷࡣ࡯࡭ࡩࠦࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠣ࡭ࡲࡧࡧࡦࠢࡥࡥࡸ࡫࠶࠵ࠢࡶࡸࡷࠨᐳ"))
                return
            bstack1ll11ll1lll_opy_ = self.bstack1l11l1l1lll_opy_(instance)
            if bstack1ll11ll1lll_opy_:
                entry = bstack1l1lllll11l_opy_(TestFramework.bstack1l11l1l11l1_opy_, screenshot)
                self.bstack1l1lll1ll1l_opy_(bstack1ll11ll1lll_opy_, [entry])
                instance.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠨ࡯࠲࠳ࡼ࠾ࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡥࡹࡧࡦࡹࡹ࡫ࠢᐴ"), datetime.now() - bstack1l111ll1lll_opy_)
            else:
                self.logger.warning(bstack11l1111_opy_ (u"ࠢࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡴࡦࡵࡷࠤ࡫ࡵࡲࠡࡹ࡫࡭ࡨ࡮ࠠࡵࡪ࡬ࡷࠥࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠢࡺࡥࡸࠦࡴࡢ࡭ࡨࡲࠥࡨࡹࠡࡦࡵ࡭ࡻ࡫ࡲ࠾ࠢࡾࢁࠧᐵ").format(instance.ref()))
        event = {}
        bstack1ll11ll1lll_opy_ = self.bstack1l11l1l1lll_opy_(instance)
        if bstack1ll11ll1lll_opy_:
            self.bstack1l111llll11_opy_(event, bstack1ll11ll1lll_opy_)
            if event.get(bstack11l1111_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨᐶ")):
                self.bstack1l1lll1ll1l_opy_(bstack1ll11ll1lll_opy_, event[bstack11l1111_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᐷ")])
            else:
                self.logger.debug(bstack11l1111_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢ࡯ࡳ࡬ࡹࠠࡧࡱࡵࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࠡࡧࡹࡩࡳࡺࠢᐸ"))
    @measure(event_name=EVENTS.bstack1l11l11ll1l_opy_, stage=STAGE.bstack1111ll111_opy_)
    def bstack1l1lll1ll1l_opy_(
        self,
        bstack1ll11ll1lll_opy_: bstack1lll1ll11ll_opy_,
        entries: List[bstack1l1lllll11l_opy_],
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1llll11ll1l_opy_)
        req.execution_context.hash = str(bstack1ll11ll1lll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11ll1lll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11ll1lll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1lll1l1111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1lll1l11111_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1lll11ll111_opy_)
            log_entry.test_framework_state = bstack1ll11ll1lll_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l1111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᐹ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11l1111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᐺ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1lll1llll_opy_
                log_entry.file_path = entry.bstack1l1ll_opy_
        def bstack1ll1l11l111_opy_():
            bstack11ll111l1_opy_ = datetime.now()
            try:
                self.bstack1llll1l1lll_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l1l11l1_opy_:
                    bstack1ll11ll1lll_opy_.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᐻ"), datetime.now() - bstack11ll111l1_opy_)
                elif entry.kind == TestFramework.bstack1l11l1lll1l_opy_:
                    bstack1ll11ll1lll_opy_.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦᐼ"), datetime.now() - bstack11ll111l1_opy_)
                else:
                    bstack1ll11ll1lll_opy_.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠ࡮ࡲ࡫ࠧᐽ"), datetime.now() - bstack11ll111l1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᐾ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1111_opy_.enqueue(bstack1ll1l11l111_opy_)
    @measure(event_name=EVENTS.bstack1l11l1ll111_opy_, stage=STAGE.bstack1111ll111_opy_)
    def bstack1l111lll1l1_opy_(
        self,
        instance: bstack1lll1ll11ll_opy_,
        bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_],
        event_json=None,
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll11ll1l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l1111l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11111_opy_)
        req.test_framework_state = bstack1llllll1lll_opy_[0].name
        req.test_hook_state = bstack1llllll1lll_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll111ll11l_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1l1lll1ll11_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l111ll1ll1_opy_)).encode(bstack11l1111_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᐿ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll1l11l111_opy_():
            bstack11ll111l1_opy_ = datetime.now()
            try:
                self.bstack1llll1l1lll_opy_.TestFrameworkEvent(req)
                instance.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡶࡩࡳࡪ࡟ࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡧࡹࡩࡳࡺࠢᑀ"), datetime.now() - bstack11ll111l1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1111_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᑁ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11l1111_opy_.enqueue(bstack1ll1l11l111_opy_)
    def bstack1l11l1l1lll_opy_(self, instance: bstack1llll1ll11l_opy_):
        bstack1l11l1ll11l_opy_ = TestFramework.bstack1l11l1ll1l1_opy_(instance.context)
        for t in bstack1l11l1ll11l_opy_:
            bstack1lll1111l1l_opy_ = TestFramework.get_state(t, bstack1lll1111l11_opy_.bstack1llll111111_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111l1l_opy_):
                return t
    def bstack1l11l1ll1ll_opy_(self, message):
        self.bstack1l11l11llll_opy_(message + bstack11l1111_opy_ (u"ࠨ࡜࡯ࠤᑂ"))
    def log_error(self, message):
        self.bstack1l11l111lll_opy_(message + bstack11l1111_opy_ (u"ࠢ࡝ࡰࠥᑃ"))
    def bstack1l11l111l11_opy_(self, level, original_func):
        def bstack1l11l1l1l1l_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack11l1111_opy_ (u"ࠣࡇࡹࡩࡳࡺࡄࡪࡵࡳࡥࡹࡩࡨࡦࡴࡐࡳࡩࡻ࡬ࡦࠤᑄ") in message or bstack11l1111_opy_ (u"ࠤ࡞ࡗࡉࡑࡃࡍࡋࡠࠦᑅ") in message or bstack11l1111_opy_ (u"ࠥ࡟࡜࡫ࡢࡅࡴ࡬ࡺࡪࡸࡍࡰࡦࡸࡰࡪࡣࠢᑆ") in message:
                return return_value
            bstack1l11l1ll11l_opy_ = TestFramework.bstack1l111lll111_opy_()
            if not bstack1l11l1ll11l_opy_:
                return return_value
            bstack1ll11ll1lll_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l1ll11l_opy_
                    if TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1lll11ll111_opy_)
                ),
                None,
            )
            if not bstack1ll11ll1lll_opy_:
                return return_value
            entry = bstack1l1lllll11l_opy_(TestFramework.bstack1ll11ll1ll1_opy_, message, level)
            self.bstack1l1lll1ll1l_opy_(bstack1ll11ll1lll_opy_, [entry])
            return return_value
        return bstack1l11l1l1l1l_opy_
    def bstack1l11l11lll1_opy_(self):
        def bstack1l11l1l1111_opy_(*args, **kwargs):
            try:
                self.bstack1l11l1l1l11_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack11l1111_opy_ (u"ࠫࠥ࠭ᑇ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack11l1111_opy_ (u"ࠧࡋࡶࡦࡰࡷࡈ࡮ࡹࡰࡢࡶࡦ࡬ࡪࡸࡍࡰࡦࡸࡰࡪࠨᑈ") in message:
                    return
                bstack1l11l1ll11l_opy_ = TestFramework.bstack1l111lll111_opy_()
                if not bstack1l11l1ll11l_opy_:
                    return
                bstack1ll11ll1lll_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l1ll11l_opy_
                        if TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1lll11ll111_opy_)
                    ),
                    None,
                )
                if not bstack1ll11ll1lll_opy_:
                    return
                entry = bstack1l1lllll11l_opy_(TestFramework.bstack1ll11ll1ll1_opy_, message, bstack1l1l11ll111_opy_.bstack1l11l111l1l_opy_)
                self.bstack1l1lll1ll1l_opy_(bstack1ll11ll1lll_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l1l1l11_opy_(bstack1lll1ll1111_opy_ (u"ࠨ࡛ࡆࡸࡨࡲࡹࡊࡩࡴࡲࡤࡸࡨ࡮ࡥࡳࡏࡲࡨࡺࡲࡥ࡞ࠢࡏࡳ࡬ࠦࡣࡢࡲࡷࡹࡷ࡫ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡧࢀࠦᑉ"))
                except:
                    pass
        return bstack1l11l1l1111_opy_
    def bstack1l111llll11_opy_(self, event: dict, instance=None) -> None:
        global _1ll11l1l111_opy_
        levels = [bstack11l1111_opy_ (u"ࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥᑊ"), bstack11l1111_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᑋ")]
        bstack1l111ll11l1_opy_ = bstack11l1111_opy_ (u"ࠤࠥᑌ")
        if instance is not None:
            try:
                bstack1l111ll11l1_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll11ll111_opy_)
            except Exception as e:
                self.logger.warning(bstack11l1111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡹࡺ࡯ࡤࠡࡨࡵࡳࡲࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠣᑍ").format(e))
        bstack1l11l1lll11_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᑎ")]
                bstack1l1llll1ll1_opy_ = os.path.join(bstack1ll1111111l_opy_, (bstack1l1llllllll_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1l1llll1ll1_opy_):
                    self.logger.debug(bstack11l1111_opy_ (u"ࠧࡊࡩࡳࡧࡦࡸࡴࡸࡹࠡࡰࡲࡸࠥࡶࡲࡦࡵࡨࡲࡹࠦࡦࡰࡴࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡕࡧࡶࡸࠥࡧ࡮ࡥࠢࡅࡹ࡮ࡲࡤࠡ࡮ࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࢁࡽࠣᑏ").format(bstack1l1llll1ll1_opy_))
                    continue
                file_names = os.listdir(bstack1l1llll1ll1_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1l1llll1ll1_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll11l1l111_opy_:
                        self.logger.info(bstack11l1111_opy_ (u"ࠨࡐࡢࡶ࡫ࠤࡦࡲࡲࡦࡣࡧࡽࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡽࢀࠦᑐ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l11l1l1_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l11l1l1_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack11l1111_opy_ (u"ࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥᑑ"):
                                entry = bstack1l1lllll11l_opy_(
                                    kind=bstack11l1111_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᑒ"),
                                    message=bstack11l1111_opy_ (u"ࠤࠥᑓ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1lll1llll_opy_=file_size,
                                    bstack1ll111111l1_opy_=bstack11l1111_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥᑔ"),
                                    bstack1l1ll_opy_=os.path.abspath(file_path),
                                    bstack1l11l1l111_opy_=bstack1l111ll11l1_opy_
                                )
                            elif level == bstack11l1111_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᑕ"):
                                entry = bstack1l1lllll11l_opy_(
                                    kind=bstack11l1111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᑖ"),
                                    message=bstack11l1111_opy_ (u"ࠨࠢᑗ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1lll1llll_opy_=file_size,
                                    bstack1ll111111l1_opy_=bstack11l1111_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢᑘ"),
                                    bstack1l1ll_opy_=os.path.abspath(file_path),
                                    bstack1ll11l1ll11_opy_=bstack1l111ll11l1_opy_
                                )
                            bstack1l11l1lll11_opy_.append(entry)
                            _1ll11l1l111_opy_.add(abs_path)
                        except Exception as bstack1l111lllll1_opy_:
                            self.logger.error(bstack11l1111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡷࡧࡩࡴࡧࡧࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࢀࢃࠢᑙ").format(bstack1l111lllll1_opy_))
        except Exception as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡸࡡࡪࡵࡨࡨࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࢁࡽࠣᑚ").format(e))
        event[bstack11l1111_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᑛ")] = bstack1l11l1lll11_opy_
class bstack1l111ll1ll1_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l111ll11ll_opy_ = set()
        kwargs[bstack11l1111_opy_ (u"ࠦࡸࡱࡩࡱ࡭ࡨࡽࡸࠨᑜ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l1l1ll1_opy_(obj, self.bstack1l111ll11ll_opy_)
def bstack1l11l11l11l_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l1l1ll1_opy_(obj, bstack1l111ll11ll_opy_=None, max_depth=3):
    if bstack1l111ll11ll_opy_ is None:
        bstack1l111ll11ll_opy_ = set()
    if id(obj) in bstack1l111ll11ll_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l111ll11ll_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l111111_opy_ = TestFramework.bstack1ll1l1l11l1_opy_(obj)
    bstack1l111ll1l1l_opy_ = next((k.lower() in bstack1l11l111111_opy_.lower() for k in bstack1l111lll1ll_opy_.keys()), None)
    if bstack1l111ll1l1l_opy_:
        obj = TestFramework.bstack1ll1l1l1l1l_opy_(obj, bstack1l111lll1ll_opy_[bstack1l111ll1l1l_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11l1111_opy_ (u"ࠧࡥ࡟ࡴ࡮ࡲࡸࡸࡥ࡟ࠣᑝ")):
            keys = getattr(obj, bstack11l1111_opy_ (u"ࠨ࡟ࡠࡵ࡯ࡳࡹࡹ࡟ࡠࠤᑞ"), [])
        elif hasattr(obj, bstack11l1111_opy_ (u"ࠢࡠࡡࡧ࡭ࡨࡺ࡟ࡠࠤᑟ")):
            keys = getattr(obj, bstack11l1111_opy_ (u"ࠣࡡࡢࡨ࡮ࡩࡴࡠࡡࠥᑠ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11l1111_opy_ (u"ࠤࡢࠦᑡ"))}
        if not obj and bstack1l11l111111_opy_ == bstack11l1111_opy_ (u"ࠥࡴࡦࡺࡨ࡭࡫ࡥ࠲ࡕࡵࡳࡪࡺࡓࡥࡹ࡮ࠢᑢ"):
            obj = {bstack11l1111_opy_ (u"ࠦࡵࡧࡴࡩࠤᑣ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l11l11l_opy_(key) or str(key).startswith(bstack11l1111_opy_ (u"ࠧࡥࠢᑤ")):
            continue
        if value is not None and bstack1l11l11l11l_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l1l1ll1_opy_(value, bstack1l111ll11ll_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l1l1ll1_opy_(o, bstack1l111ll11ll_opy_, max_depth) for o in value]))
    return result or None