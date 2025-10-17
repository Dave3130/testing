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
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1111111lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1llll1l11ll_opy_,
    bstack1llll1l1l11_opy_,
    bstack1lll1llll11_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1lll_opy_, bstack11l11l11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l11_opy_ import bstack1llll1l11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_, bstack1lll1l11l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1llll11llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l1l_opy_ import bstack1llll11lll1_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11ll11l1l1_opy_ import bstack1lllll1l1l_opy_, bstack1111ll1l11_opy_, bstack1ll1l11l1_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll1l1111l_opy_(bstack1llll11lll1_opy_):
    bstack1llll11ll1l_opy_ = bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡶ࡮ࡼࡥࡳࡵࠥჱ")
    bstack1llll111ll1_opy_ = bstack11111_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦჲ")
    bstack1lll1ll11l1_opy_ = bstack11111_opy_ (u"ࠨ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣჳ")
    bstack1lll1l1lll1_opy_ = bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢჴ")
    bstack1lll1ll1l11_opy_ = bstack11111_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫࡟ࡳࡧࡩࡷࠧჵ")
    bstack1llll111l11_opy_ = bstack11111_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡤࡴࡨࡥࡹ࡫ࡤࠣჶ")
    bstack1llll111lll_opy_ = bstack11111_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨჷ")
    bstack1llll11111l_opy_ = bstack11111_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡶࡸࡦࡺࡵࡴࠤჸ")
    def __init__(self):
        super().__init__(bstack1lll1ll1ll1_opy_=self.bstack1llll11ll1l_opy_, frameworks=[bstack1llll1l11l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.BEFORE_EACH, bstack1lll1l1ll11_opy_.POST), self.bstack1lll1llllll_opy_)
        if bstack11l11l11l1_opy_():
            TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.POST), self.bstack1llll11l1ll_opy_)
        else:
            TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.PRE), self.bstack1llll11l1ll_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.POST), self.bstack1lll1l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1llllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1l111ll_opy_ = self.bstack1lll1l11ll1_opy_(instance.context)
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡳࡥ࡬࡫࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥჹ") + str(bstack1lllllll1ll_opy_) + bstack11111_opy_ (u"ࠨࠢჺ"))
            return
        f.bstack11111111ll_opy_(instance, bstack1lll1l1111l_opy_.bstack1llll111ll1_opy_, bstack1lll1l111ll_opy_)
    def bstack1lll1l11ll1_opy_(self, context: bstack1lll1llll11_opy_, bstack1lll1lll11l_opy_= True):
        if bstack1lll1lll11l_opy_:
            bstack1lll1l111ll_opy_ = self.bstack1llll11l111_opy_(context, reverse=True)
        else:
            bstack1lll1l111ll_opy_ = self.bstack1llll1l111l_opy_(context, reverse=True)
        return [f for f in bstack1lll1l111ll_opy_ if f[1].state != bstack1llllll1111_opy_.QUIT]
    def bstack1llll11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1llllll_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥ჻") + str(kwargs) + bstack11111_opy_ (u"ࠣࠤჼ"))
            return
        bstack1lll1l111ll_opy_ = f.get_state(instance, bstack1lll1l1111l_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧჽ") + str(kwargs) + bstack11111_opy_ (u"ࠥࠦჾ"))
            return
        if len(bstack1lll1l111ll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll11ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨჿ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll1111_opy_ = bstack1lll1l111ll_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄀ") + str(kwargs) + bstack11111_opy_ (u"ࠨࠢᄁ"))
            return
        bstack11l11l11ll_opy_ = getattr(args[0], bstack11111_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᄂ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᄃ")).get(bstack11111_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᄄ")):
            try:
                page.evaluate(bstack11111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᄅ"),
                            bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨᄆ") + json.dumps(
                                bstack11l11l11ll_opy_) + bstack11111_opy_ (u"ࠧࢃࡽࠣᄇ"))
            except Exception as e:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦᄈ"), e)
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1llllll_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄉ") + str(kwargs) + bstack11111_opy_ (u"ࠣࠤᄊ"))
            return
        bstack1lll1l111ll_opy_ = f.get_state(instance, bstack1lll1l1111l_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄋ") + str(kwargs) + bstack11111_opy_ (u"ࠥࠦᄌ"))
            return
        if len(bstack1lll1l111ll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll11ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᄍ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll1111_opy_ = bstack1lll1l111ll_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄎ") + str(kwargs) + bstack11111_opy_ (u"ࠨࠢᄏ"))
            return
        status = f.get_state(instance, TestFramework.bstack1llll11l1l1_opy_, None)
        if not status:
            self.logger.debug(bstack11111_opy_ (u"ࠢ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᄐ") + str(bstack1lllllll1ll_opy_) + bstack11111_opy_ (u"ࠣࠤᄑ"))
            return
        bstack1llll1111l1_opy_ = {bstack11111_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᄒ"): status.lower()}
        bstack1lll1lll1ll_opy_ = f.get_state(instance, TestFramework.bstack1llll111111_opy_, None)
        if status.lower() == bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᄓ") and bstack1lll1lll1ll_opy_ is not None:
            bstack1llll1111l1_opy_[bstack11111_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᄔ")] = bstack1lll1lll1ll_opy_[0][bstack11111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᄕ")][0] if isinstance(bstack1lll1lll1ll_opy_, list) else str(bstack1lll1lll1ll_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᄖ")).get(bstack11111_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᄗ")):
            try:
                page.evaluate(
                        bstack11111_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᄘ"),
                        bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࠧᄙ")
                        + json.dumps(bstack1llll1111l1_opy_)
                        + bstack11111_opy_ (u"ࠥࢁࠧᄚ")
                    )
            except Exception as e:
                self.logger.debug(bstack11111_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀࠦᄛ"), e)
    def bstack1lll1lllll1_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1llllll_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        if not bstack1lll1ll1lll_opy_:
            self.logger.debug(
                bstack1lll1ll11ll_opy_ (u"ࠧࡳࡡࡳ࡭ࡢࡳ࠶࠷ࡹࡠࡵࡼࡲࡨࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᄜ"))
            return
        bstack1lll1l111ll_opy_ = f.get_state(instance, bstack1lll1l1111l_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄝ") + str(kwargs) + bstack11111_opy_ (u"ࠢࠣᄞ"))
            return
        if len(bstack1lll1l111ll_opy_) > 1:
            self.logger.debug(
                bstack1lll1ll11ll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄟ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll1111_opy_ = bstack1lll1l111ll_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄠ") + str(kwargs) + bstack11111_opy_ (u"ࠥࠦᄡ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack11111_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤᄢ") + str(timestamp)
        try:
            page.evaluate(
                bstack11111_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᄣ"),
                bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᄤ").format(
                    json.dumps(
                        {
                            bstack11111_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᄥ"): bstack11111_opy_ (u"ࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥᄦ"),
                            bstack11111_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᄧ"): {
                                bstack11111_opy_ (u"ࠥࡸࡾࡶࡥࠣᄨ"): bstack11111_opy_ (u"ࠦࡆࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠣᄩ"),
                                bstack11111_opy_ (u"ࠧࡪࡡࡵࡣࠥᄪ"): data,
                                bstack11111_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࠧᄫ"): bstack11111_opy_ (u"ࠢࡥࡧࡥࡹ࡬ࠨᄬ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack11111_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡴ࠷࠱ࡺࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡼࡿࠥᄭ"), e)
    def bstack1llll11l11l_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1llllll_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll1l1111l_opy_.bstack1llll111l11_opy_, False):
            return
        self.bstack1lllll1lll1_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll1111l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll111l1l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l111l1_opy_)
        req.test_framework_state = bstack1lllllll1ll_opy_[0].name
        req.test_hook_state = bstack1lllllll1ll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11lllll_opy_)
        for bstack1lll1l1l11l_opy_ in bstack1llll11llll_opy_.bstack1lll1l11111_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack11111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣᄮ")
                if bstack1lll1ll1lll_opy_
                else bstack11111_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠤᄯ")
            )
            session.ref = bstack1lll1l1l11l_opy_.ref()
            session.hub_url = bstack1llll11llll_opy_.get_state(bstack1lll1l1l11l_opy_, bstack1llll11llll_opy_.bstack1llll1l1111_opy_, bstack11111_opy_ (u"ࠦࠧᄰ"))
            session.framework_name = bstack1lll1l1l11l_opy_.framework_name
            session.framework_version = bstack1lll1l1l11l_opy_.framework_version
            session.framework_session_id = bstack1llll11llll_opy_.get_state(bstack1lll1l1l11l_opy_, bstack1llll11llll_opy_.bstack1lll1l1ll1l_opy_, bstack11111_opy_ (u"ࠧࠨᄱ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1l111ll_opy_ = f.get_state(instance, bstack1lll1l1111l_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1l111ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄲ") + str(kwargs) + bstack11111_opy_ (u"ࠢࠣᄳ"))
            return
        if len(bstack1lll1l111ll_opy_) > 1:
            self.logger.debug(bstack11111_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄴ") + str(kwargs) + bstack11111_opy_ (u"ࠤࠥᄵ"))
        bstack1lll1l11l1l_opy_, bstack1lll1ll1111_opy_ = bstack1lll1l111ll_opy_[0]
        page = bstack1lll1l11l1l_opy_()
        if not page:
            self.logger.debug(bstack11111_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄶ") + str(kwargs) + bstack11111_opy_ (u"ࠦࠧᄷ"))
            return
        return page
    def bstack1lll1l1llll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll1111ll_opy_ = {}
        for bstack1lll1l1l11l_opy_ in bstack1llll11llll_opy_.bstack1lll1l11111_opy_.values():
            caps = bstack1llll11llll_opy_.get_state(bstack1lll1l1l11l_opy_, bstack1llll11llll_opy_.bstack1lll1l1l111_opy_, bstack11111_opy_ (u"ࠧࠨᄸ"))
        bstack1llll1111ll_opy_[bstack11111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦᄹ")] = caps.get(bstack11111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣᄺ"), bstack11111_opy_ (u"ࠣࠤᄻ"))
        bstack1llll1111ll_opy_[bstack11111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣᄼ")] = caps.get(bstack11111_opy_ (u"ࠥࡳࡸࠨᄽ"), bstack11111_opy_ (u"ࠦࠧᄾ"))
        bstack1llll1111ll_opy_[bstack11111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᄿ")] = caps.get(bstack11111_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥᅀ"), bstack11111_opy_ (u"ࠢࠣᅁ"))
        bstack1llll1111ll_opy_[bstack11111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤᅂ")] = caps.get(bstack11111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦᅃ"), bstack11111_opy_ (u"ࠥࠦᅄ"))
        return bstack1llll1111ll_opy_
    def bstack1lll1l11lll_opy_(self, page: object, bstack1lll1lll1l1_opy_, args={}):
        try:
            bstack1llll11ll11_opy_ = bstack11111_opy_ (u"ࠦࠧࠨࠨࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࠫ࠲࠳࠴ࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸ࠯ࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥࡴࡥࡸࠢࡓࡶࡴࡳࡩࡴࡧࠫࠬࡷ࡫ࡳࡰ࡮ࡹࡩ࠱ࠦࡲࡦ࡬ࡨࡧࡹ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷ࠳ࡶࡵࡴࡪࠫࡶࡪࡹ࡯࡭ࡸࡨ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢁࡦ࡯ࡡࡥࡳࡩࡿࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࡾࠫࠫࡿࡦࡸࡧࡠ࡬ࡶࡳࡳࢃࠩࠣࠤࠥᅅ")
            bstack1lll1lll1l1_opy_ = bstack1lll1lll1l1_opy_.replace(bstack11111_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᅆ"), bstack11111_opy_ (u"ࠨࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸࠨᅇ"))
            script = bstack1llll11ll11_opy_.format(fn_body=bstack1lll1lll1l1_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠢࡢ࠳࠴ࡽࡤࡹࡣࡳ࡫ࡳࡸࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡆࡴࡵࡳࡷࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷ࠰ࠥࠨᅈ") + str(e) + bstack11111_opy_ (u"ࠣࠤᅉ"))