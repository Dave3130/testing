# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
    bstack1lllll11l1l_opy_,
    bstack1lll1l1111l_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1l1l_opy_, bstack1ll11111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111lll_opy_, bstack1lll1lll11l_opy_, bstack1lll1lll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l11lll_opy_ import bstack1llll11l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import bstack1lll1l1l1ll_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l11111ll1_opy_ import bstack111lllllll_opy_, bstack1ll111l1ll_opy_, bstack111ll1lll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1llll11llll_opy_(bstack1lll1l1l1ll_opy_):
    bstack1lll1ll111l_opy_ = bstack111111l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡦࡵ࡭ࡻ࡫ࡲࡴࠤჷ")
    bstack1lll1l1l11l_opy_ = bstack111111l_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥჸ")
    bstack1lll1lll111_opy_ = bstack111111l_opy_ (u"ࠧࡴ࡯࡯ࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢჹ")
    bstack1lll1l11l1l_opy_ = bstack111111l_opy_ (u"ࠨࡴࡦࡵࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨჺ")
    bstack1lll1llllll_opy_ = bstack111111l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡥࡲࡦࡨࡶࠦ჻")
    bstack1llll11111l_opy_ = bstack111111l_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡣࡳࡧࡤࡸࡪࡪࠢჼ")
    bstack1lll1l1l111_opy_ = bstack111111l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟࡯ࡣࡰࡩࠧჽ")
    bstack1lll1l11ll1_opy_ = bstack111111l_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡵࡷࡥࡹࡻࡳࠣჾ")
    def __init__(self):
        super().__init__(bstack1lll1lllll1_opy_=self.bstack1lll1ll111l_opy_, frameworks=[bstack1llllll11ll_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.BEFORE_EACH, bstack1lll1lll11l_opy_.POST), self.bstack1lll1ll1l11_opy_)
        if bstack1ll11111l1_opy_():
            TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1lll1ll1lll_opy_)
        else:
            TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.PRE), self.bstack1lll1ll1lll_opy_)
        TestFramework.bstack1111111l11_opy_((bstack1llll111lll_opy_.TEST, bstack1lll1lll11l_opy_.POST), self.bstack1llll11l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1ll1l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1l111ll_opy_ = self.bstack1lll1l1llll_opy_(instance.context)
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡲࡤ࡫ࡪࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤჿ") + str(bstack1lllll1l1ll_opy_) + bstack111111l_opy_ (u"ࠧࠨᄀ"))
            return
        f.bstack1llll1lll1l_opy_(instance, bstack1llll11llll_opy_.bstack1lll1l1l11l_opy_, bstack1lll1l111ll_opy_)
    def bstack1lll1l1llll_opy_(self, context: bstack1lll1l1111l_opy_, bstack1llll1l111l_opy_= True):
        if bstack1llll1l111l_opy_:
            bstack1lll1l111ll_opy_ = self.bstack1llll111l11_opy_(context, reverse=True)
        else:
            bstack1lll1l111ll_opy_ = self.bstack1llll111111_opy_(context, reverse=True)
        return [f for f in bstack1lll1l111ll_opy_ if f[1].state != bstack1llll1lllll_opy_.QUIT]
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1l11_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄁ") + str(kwargs) + bstack111111l_opy_ (u"ࠢࠣᄂ"))
            return
        bstack1lll1l111ll_opy_ = f.get_state(instance, bstack1llll11llll_opy_.bstack1lll1l1l11l_opy_, [])
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄃ") + str(kwargs) + bstack111111l_opy_ (u"ࠤࠥᄄ"))
            return
        if len(bstack1lll1l111ll_opy_) > 1:
            self.logger.debug(
                bstack1llll1ll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᄅ"))
        bstack1llll1l1111_opy_, bstack1lll1l111l1_opy_ = bstack1lll1l111ll_opy_[0]
        page = bstack1llll1l1111_opy_()
        if not page:
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄆ") + str(kwargs) + bstack111111l_opy_ (u"ࠧࠨᄇ"))
            return
        bstack1l111l1ll_opy_ = getattr(args[0], bstack111111l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᄈ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack111111l_opy_ (u"ࠢࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠧᄉ")).get(bstack111111l_opy_ (u"ࠣࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥᄊ")):
            try:
                page.evaluate(bstack111111l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᄋ"),
                            bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧᄌ") + json.dumps(
                                bstack1l111l1ll_opy_) + bstack111111l_opy_ (u"ࠦࢂࢃࠢᄍ"))
            except Exception as e:
                self.logger.debug(bstack111111l_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥᄎ"), e)
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1l11_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄏ") + str(kwargs) + bstack111111l_opy_ (u"ࠢࠣᄐ"))
            return
        bstack1lll1l111ll_opy_ = f.get_state(instance, bstack1llll11llll_opy_.bstack1lll1l1l11l_opy_, [])
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄑ") + str(kwargs) + bstack111111l_opy_ (u"ࠤࠥᄒ"))
            return
        if len(bstack1lll1l111ll_opy_) > 1:
            self.logger.debug(
                bstack1llll1ll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࢁ࡬ࡦࡰࠫࡴࡦ࡭ࡥࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᄓ"))
        bstack1llll1l1111_opy_, bstack1lll1l111l1_opy_ = bstack1lll1l111ll_opy_[0]
        page = bstack1llll1l1111_opy_()
        if not page:
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡳࡥ࡬࡫ࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄔ") + str(kwargs) + bstack111111l_opy_ (u"ࠧࠨᄕ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1ll1ll1_opy_, None)
        if not status:
            self.logger.debug(bstack111111l_opy_ (u"ࠨ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᄖ") + str(bstack1lllll1l1ll_opy_) + bstack111111l_opy_ (u"ࠢࠣᄗ"))
            return
        bstack1lll1l1l1l1_opy_ = {bstack111111l_opy_ (u"ࠣࡵࡷࡥࡹࡻࡳࠣᄘ"): status.lower()}
        bstack1lll1ll11l1_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_, None)
        if status.lower() == bstack111111l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᄙ") and bstack1lll1ll11l1_opy_ is not None:
            bstack1lll1l1l1l1_opy_[bstack111111l_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᄚ")] = bstack1lll1ll11l1_opy_[0][bstack111111l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᄛ")][0] if isinstance(bstack1lll1ll11l1_opy_, list) else str(bstack1lll1ll11l1_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᄜ")).get(bstack111111l_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᄝ")):
            try:
                page.evaluate(
                        bstack111111l_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᄞ"),
                        bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥ࠭ᄟ")
                        + json.dumps(bstack1lll1l1l1l1_opy_)
                        + bstack111111l_opy_ (u"ࠤࢀࠦᄠ")
                    )
            except Exception as e:
                self.logger.debug(bstack111111l_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡼࡿࠥᄡ"), e)
    def bstack1llll111ll1_opy_(
        self,
        instance: bstack1lll1lll1l1_opy_,
        f: TestFramework,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1l11_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        if not bstack1lll1ll1l1l_opy_:
            self.logger.debug(
                bstack1llll1ll1_opy_ (u"ࠦࡲࡧࡲ࡬ࡡࡲ࠵࠶ࡿ࡟ࡴࡻࡱࡧ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧᄢ"))
            return
        bstack1lll1l111ll_opy_ = f.get_state(instance, bstack1llll11llll_opy_.bstack1lll1l1l11l_opy_, [])
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄣ") + str(kwargs) + bstack111111l_opy_ (u"ࠨࠢᄤ"))
            return
        if len(bstack1lll1l111ll_opy_) > 1:
            self.logger.debug(
                bstack1llll1ll1_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤᄥ"))
        bstack1llll1l1111_opy_, bstack1lll1l111l1_opy_ = bstack1lll1l111ll_opy_[0]
        page = bstack1llll1l1111_opy_()
        if not page:
            self.logger.debug(bstack111111l_opy_ (u"ࠣ࡯ࡤࡶࡰࡥ࡯࠲࠳ࡼࡣࡸࡿ࡮ࡤ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄦ") + str(kwargs) + bstack111111l_opy_ (u"ࠤࠥᄧ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack111111l_opy_ (u"ࠥࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡖࡽࡳࡩ࠺ࠣᄨ") + str(timestamp)
        try:
            page.evaluate(
                bstack111111l_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᄩ"),
                bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᄪ").format(
                    json.dumps(
                        {
                            bstack111111l_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᄫ"): bstack111111l_opy_ (u"ࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤᄬ"),
                            bstack111111l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᄭ"): {
                                bstack111111l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᄮ"): bstack111111l_opy_ (u"ࠥࡅࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠢᄯ"),
                                bstack111111l_opy_ (u"ࠦࡩࡧࡴࡢࠤᄰ"): data,
                                bstack111111l_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࠦᄱ"): bstack111111l_opy_ (u"ࠨࡤࡦࡤࡸ࡫ࠧᄲ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack111111l_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡳ࠶࠷ࡹࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡻࡾࠤᄳ"), e)
    def bstack1lll1llll11_opy_(
        self,
        instance: bstack1lll1lll1l1_opy_,
        f: TestFramework,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1l11_opy_(f, instance, bstack1lllll1l1ll_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1llll11llll_opy_.bstack1llll11111l_opy_, False):
            return
        self.bstack1llll1l1ll1_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllll1l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1llll1l11l1_opy_)
        req.test_framework_state = bstack1lllll1l1ll_opy_[0].name
        req.test_hook_state = bstack1lllll1l1ll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11lll1_opy_)
        for bstack1lll1l1lll1_opy_ in bstack1llll11l1ll_opy_.bstack1llll111l1l_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack111111l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢᄴ")
                if bstack1lll1ll1l1l_opy_
                else bstack111111l_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠣᄵ")
            )
            session.ref = bstack1lll1l1lll1_opy_.ref()
            session.hub_url = bstack1llll11l1ll_opy_.get_state(bstack1lll1l1lll1_opy_, bstack1llll11l1ll_opy_.bstack1llll11ll11_opy_, bstack111111l_opy_ (u"ࠥࠦᄶ"))
            session.framework_name = bstack1lll1l1lll1_opy_.framework_name
            session.framework_version = bstack1lll1l1lll1_opy_.framework_version
            session.framework_session_id = bstack1llll11l1ll_opy_.get_state(bstack1lll1l1lll1_opy_, bstack1llll11l1ll_opy_.bstack1lll1lll1ll_opy_, bstack111111l_opy_ (u"ࠦࠧᄷ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1llll1111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1l111ll_opy_ = f.get_state(instance, bstack1llll11llll_opy_.bstack1lll1l1l11l_opy_, [])
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack111111l_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄸ") + str(kwargs) + bstack111111l_opy_ (u"ࠨࠢᄹ"))
            return
        if len(bstack1lll1l111ll_opy_) > 1:
            self.logger.debug(bstack111111l_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᄺ") + str(kwargs) + bstack111111l_opy_ (u"ࠣࠤᄻ"))
        bstack1llll1l1111_opy_, bstack1lll1l111l1_opy_ = bstack1lll1l111ll_opy_[0]
        page = bstack1llll1l1111_opy_()
        if not page:
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄼ") + str(kwargs) + bstack111111l_opy_ (u"ࠥࠦᄽ"))
            return
        return page
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1l1_opy_,
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll11l1l1_opy_ = {}
        for bstack1lll1l1lll1_opy_ in bstack1llll11l1ll_opy_.bstack1llll111l1l_opy_.values():
            caps = bstack1llll11l1ll_opy_.get_state(bstack1lll1l1lll1_opy_, bstack1llll11l1ll_opy_.bstack1lll1l1ll11_opy_, bstack111111l_opy_ (u"ࠦࠧᄾ"))
        bstack1llll11l1l1_opy_[bstack111111l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥᄿ")] = caps.get(bstack111111l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢᅀ"), bstack111111l_opy_ (u"ࠢࠣᅁ"))
        bstack1llll11l1l1_opy_[bstack111111l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢᅂ")] = caps.get(bstack111111l_opy_ (u"ࠤࡲࡷࠧᅃ"), bstack111111l_opy_ (u"ࠥࠦᅄ"))
        bstack1llll11l1l1_opy_[bstack111111l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨᅅ")] = caps.get(bstack111111l_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤᅆ"), bstack111111l_opy_ (u"ࠨࠢᅇ"))
        bstack1llll11l1l1_opy_[bstack111111l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣᅈ")] = caps.get(bstack111111l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥᅉ"), bstack111111l_opy_ (u"ࠤࠥᅊ"))
        return bstack1llll11l1l1_opy_
    def bstack1llll11l11l_opy_(self, page: object, bstack1lll1ll1111_opy_, args={}):
        try:
            bstack1lll1l1ll1l_opy_ = bstack111111l_opy_ (u"ࠥࠦࠧ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࠪ࠱࠲࠳ࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷ࠮ࠦࡻࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡳ࡫ࡷࠡࡒࡵࡳࡲ࡯ࡳࡦࠪࠫࡶࡪࡹ࡯࡭ࡸࡨ࠰ࠥࡸࡥ࡫ࡧࡦࡸ࠮ࠦ࠽࠿ࠢࡾࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶ࠲ࡵࡻࡳࡩࠪࡵࡩࡸࡵ࡬ࡷࡧࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢀ࡬࡮ࡠࡤࡲࡨࡾࢃࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࢁ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࡽࠪࠪࡾࡥࡷ࡭࡟࡫ࡵࡲࡲࢂ࠯ࠢࠣࠤᅋ")
            bstack1lll1ll1111_opy_ = bstack1lll1ll1111_opy_.replace(bstack111111l_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᅌ"), bstack111111l_opy_ (u"ࠧࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷࠧᅍ"))
            script = bstack1lll1l1ll1l_opy_.format(fn_body=bstack1lll1ll1111_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠨࡡ࠲࠳ࡼࡣࡸࡩࡲࡪࡲࡷࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡅࡳࡴࡲࡶࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶ࠯ࠤࠧᅎ") + str(e) + bstack111111l_opy_ (u"ࠢࠣᅏ"))