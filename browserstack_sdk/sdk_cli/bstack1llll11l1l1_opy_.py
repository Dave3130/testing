# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
    bstack1llllllll1l_opy_,
    bstack1lll1l1ll1l_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1llll1l_opy_, bstack111ll1llll_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll11l11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_, bstack1lll1l1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1l1lll1_opy_ import bstack1lll1l1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1lll_opy_ import bstack1lll1ll1l11_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack11ll1l1l1l_opy_ import bstack11l11111l_opy_, bstack1ll11111l_opy_, bstack1ll1l1ll1_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1llll1l111l_opy_(bstack1lll1ll1l11_opy_):
    bstack1llll11lll1_opy_ = bstack1ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡤࡳ࡫ࡹࡩࡷࡹࠢჼ")
    bstack1llll1l11l1_opy_ = bstack1ll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣჽ")
    bstack1lll1ll111l_opy_ = bstack1ll1l_opy_ (u"ࠥࡲࡴࡴ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧჾ")
    bstack1lll1l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦჿ")
    bstack1lll1l1l1l1_opy_ = bstack1ll1l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡣࡷ࡫ࡦࡴࠤᄀ")
    bstack1llll11ll11_opy_ = bstack1ll1l_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡨࡸࡥࡢࡶࡨࡨࠧᄁ")
    bstack1lll1lll111_opy_ = bstack1ll1l_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᄂ")
    bstack1llll111l11_opy_ = bstack1ll1l_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡳࡵࡣࡷࡹࡸࠨᄃ")
    def __init__(self):
        super().__init__(bstack1lll1ll1ll1_opy_=self.bstack1llll11lll1_opy_, frameworks=[bstack1lllll11l11_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.BEFORE_EACH, bstack1lll1llll11_opy_.POST), self.bstack1lll1ll1111_opy_)
        if bstack111ll1llll_opy_():
            TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.POST), self.bstack1llll11111l_opy_)
        else:
            TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.PRE), self.bstack1llll11111l_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.POST), self.bstack1llll11l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1ll1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1l11ll1_opy_ = self.bstack1llll111111_opy_(instance.context)
        if not bstack1lll1l11ll1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡰࡢࡩࡨ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᄄ") + str(bstack1llllll111l_opy_) + bstack1ll1l_opy_ (u"ࠥࠦᄅ"))
            return
        f.bstack1111111ll1_opy_(instance, bstack1llll1l111l_opy_.bstack1llll1l11l1_opy_, bstack1lll1l11ll1_opy_)
    def bstack1llll111111_opy_(self, context: bstack1lll1l1ll1l_opy_, bstack1lll1lll11l_opy_= True):
        if bstack1lll1lll11l_opy_:
            bstack1lll1l11ll1_opy_ = self.bstack1lll1lll1l1_opy_(context, reverse=True)
        else:
            bstack1lll1l11ll1_opy_ = self.bstack1lll1l111l1_opy_(context, reverse=True)
        return [f for f in bstack1lll1l11ll1_opy_ if f[1].state != bstack1lllll11l1l_opy_.QUIT]
    def bstack1llll11111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1111_opy_(f, instance, bstack1llllll111l_opy_, *args, **kwargs)
        if not bstack1lll1llll1l_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄆ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠧࠨᄇ"))
            return
        bstack1lll1l11ll1_opy_ = f.get_state(instance, bstack1llll1l111l_opy_.bstack1llll1l11l1_opy_, [])
        if not bstack1lll1l11ll1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄈ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠢࠣᄉ"))
            return
        if len(bstack1lll1l11ll1_opy_) > 1:
            self.logger.debug(
                bstack1lllll1l1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄊ"))
        bstack1lll1l111ll_opy_, bstack1lll1ll1l1l_opy_ = bstack1lll1l11ll1_opy_[0]
        page = bstack1lll1l111ll_opy_()
        if not page:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄋ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠥࠦᄌ"))
            return
        bstack1llll111ll_opy_ = getattr(args[0], bstack1ll1l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᄍ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠥᄎ")).get(bstack1ll1l_opy_ (u"ࠨࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᄏ")):
            try:
                page.evaluate(bstack1ll1l_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᄐ"),
                            bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠬᄑ") + json.dumps(
                                bstack1llll111ll_opy_) + bstack1ll1l_opy_ (u"ࠤࢀࢁࠧᄒ"))
            except Exception as e:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽࠣᄓ"), e)
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1111_opy_(f, instance, bstack1llllll111l_opy_, *args, **kwargs)
        if not bstack1lll1llll1l_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᄔ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠧࠨᄕ"))
            return
        bstack1lll1l11ll1_opy_ = f.get_state(instance, bstack1llll1l111l_opy_.bstack1llll1l11l1_opy_, [])
        if not bstack1lll1l11ll1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄖ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠢࠣᄗ"))
            return
        if len(bstack1lll1l11ll1_opy_) > 1:
            self.logger.debug(
                bstack1lllll1l1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄘ"))
        bstack1lll1l111ll_opy_, bstack1lll1ll1l1l_opy_ = bstack1lll1l11ll1_opy_[0]
        page = bstack1lll1l111ll_opy_()
        if not page:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᄙ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠥࠦᄚ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1l11l1l_opy_, None)
        if not status:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡳࡵࠠࡴࡶࡤࡸࡺࡹࠠࡧࡱࡵࠤࡹ࡫ࡳࡵ࠮ࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࠢᄛ") + str(bstack1llllll111l_opy_) + bstack1ll1l_opy_ (u"ࠧࠨᄜ"))
            return
        bstack1llll111ll1_opy_ = {bstack1ll1l_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨᄝ"): status.lower()}
        bstack1llll1l1111_opy_ = f.get_state(instance, TestFramework.bstack1llll1111ll_opy_, None)
        if status.lower() == bstack1ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᄞ") and bstack1llll1l1111_opy_ is not None:
            bstack1llll111ll1_opy_[bstack1ll1l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨᄟ")] = bstack1llll1l1111_opy_[0][bstack1ll1l_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᄠ")][0] if isinstance(bstack1llll1l1111_opy_, list) else str(bstack1llll1l1111_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᄡ")).get(bstack1ll1l_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᄢ")):
            try:
                page.evaluate(
                        bstack1ll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᄣ"),
                        bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࠫᄤ")
                        + json.dumps(bstack1llll111ll1_opy_)
                        + bstack1ll1l_opy_ (u"ࠢࡾࠤᄥ")
                    )
            except Exception as e:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥࢁࡽࠣᄦ"), e)
    def bstack1lll1lll1ll_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        f: TestFramework,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1111_opy_(f, instance, bstack1llllll111l_opy_, *args, **kwargs)
        if not bstack1lll1llll1l_opy_:
            self.logger.debug(
                bstack1lllll1l1_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᄧ"))
            return
        bstack1lll1l11ll1_opy_ = f.get_state(instance, bstack1llll1l111l_opy_.bstack1llll1l11l1_opy_, [])
        if not bstack1lll1l11ll1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄨ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠦࠧᄩ"))
            return
        if len(bstack1lll1l11ll1_opy_) > 1:
            self.logger.debug(
                bstack1lllll1l1_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢᄪ"))
        bstack1lll1l111ll_opy_, bstack1lll1ll1l1l_opy_ = bstack1lll1l11ll1_opy_[0]
        page = bstack1lll1l111ll_opy_()
        if not page:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨ࡭ࡢࡴ࡮ࡣࡴ࠷࠱ࡺࡡࡶࡽࡳࡩ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄫ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠢࠣᄬ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1ll1l_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᄭ") + str(timestamp)
        try:
            page.evaluate(
                bstack1ll1l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᄮ"),
                bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨᄯ").format(
                    json.dumps(
                        {
                            bstack1ll1l_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦᄰ"): bstack1ll1l_opy_ (u"ࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢᄱ"),
                            bstack1ll1l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤᄲ"): {
                                bstack1ll1l_opy_ (u"ࠢࡵࡻࡳࡩࠧᄳ"): bstack1ll1l_opy_ (u"ࠣࡃࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠧᄴ"),
                                bstack1ll1l_opy_ (u"ࠤࡧࡥࡹࡧࠢᄵ"): data,
                                bstack1ll1l_opy_ (u"ࠥࡰࡪࡼࡥ࡭ࠤᄶ"): bstack1ll1l_opy_ (u"ࠦࡩ࡫ࡢࡶࡩࠥᄷ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡱ࠴࠵ࡾࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࢀࢃࠢᄸ"), e)
    def bstack1lll1l1l111_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        f: TestFramework,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1ll1111_opy_(f, instance, bstack1llllll111l_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1llll1l111l_opy_.bstack1llll11ll11_opy_, False):
            return
        self.bstack1lllll1l111_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllllllll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11llll_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        req.test_framework_state = bstack1llllll111l_opy_[0].name
        req.test_hook_state = bstack1llllll111l_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll11ll1l_opy_)
        for bstack1lll1l11lll_opy_ in bstack1lll1l1ll11_opy_.bstack1lll1ll11ll_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1ll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧᄹ")
                if bstack1lll1llll1l_opy_
                else bstack1ll1l_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩࠨᄺ")
            )
            session.ref = bstack1lll1l11lll_opy_.ref()
            session.hub_url = bstack1lll1l1ll11_opy_.get_state(bstack1lll1l11lll_opy_, bstack1lll1l1ll11_opy_.bstack1llll11l11l_opy_, bstack1ll1l_opy_ (u"ࠣࠤᄻ"))
            session.framework_name = bstack1lll1l11lll_opy_.framework_name
            session.framework_version = bstack1lll1l11lll_opy_.framework_version
            session.framework_session_id = bstack1lll1l1ll11_opy_.get_state(bstack1lll1l11lll_opy_, bstack1lll1l1ll11_opy_.bstack1lll1l1llll_opy_, bstack1ll1l_opy_ (u"ࠤࠥᄼ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1llllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1l11ll1_opy_ = f.get_state(instance, bstack1llll1l111l_opy_.bstack1llll1l11l1_opy_, [])
        if not bstack1lll1l11ll1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᄽ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠦࠧᄾ"))
            return
        if len(bstack1lll1l11ll1_opy_) > 1:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᄿ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠨࠢᅀ"))
        bstack1lll1l111ll_opy_, bstack1lll1ll1l1l_opy_ = bstack1lll1l11ll1_opy_[0]
        page = bstack1lll1l111ll_opy_()
        if not page:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡱࡳࠥࡶࡡࡨࡧࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅁ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠣࠤᅂ"))
            return
        return page
    def bstack1lll1lllll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1lll1ll11l1_opy_ = {}
        for bstack1lll1l11lll_opy_ in bstack1lll1l1ll11_opy_.bstack1lll1ll11ll_opy_.values():
            caps = bstack1lll1l1ll11_opy_.get_state(bstack1lll1l11lll_opy_, bstack1lll1l1ll11_opy_.bstack1lll1l1111l_opy_, bstack1ll1l_opy_ (u"ࠤࠥᅃ"))
        bstack1lll1ll11l1_opy_[bstack1ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣᅄ")] = caps.get(bstack1ll1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧᅅ"), bstack1ll1l_opy_ (u"ࠧࠨᅆ"))
        bstack1lll1ll11l1_opy_[bstack1ll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧᅇ")] = caps.get(bstack1ll1l_opy_ (u"ࠢࡰࡵࠥᅈ"), bstack1ll1l_opy_ (u"ࠣࠤᅉ"))
        bstack1lll1ll11l1_opy_[bstack1ll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦᅊ")] = caps.get(bstack1ll1l_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢᅋ"), bstack1ll1l_opy_ (u"ࠦࠧᅌ"))
        bstack1lll1ll11l1_opy_[bstack1ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨᅍ")] = caps.get(bstack1ll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣᅎ"), bstack1ll1l_opy_ (u"ࠢࠣᅏ"))
        return bstack1lll1ll11l1_opy_
    def bstack1llll1111l1_opy_(self, page: object, bstack1llll111lll_opy_, args={}):
        try:
            bstack1llll111l1l_opy_ = bstack1ll1l_opy_ (u"ࠣࠤࠥࠬ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࠨ࠯࠰࠱ࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠬࠤࢀࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡱࡩࡼࠦࡐࡳࡱࡰ࡭ࡸ࡫ࠨࠩࡴࡨࡷࡴࡲࡶࡦ࠮ࠣࡶࡪࡰࡥࡤࡶࠬࠤࡂࡄࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡷࡹࡧࡣ࡬ࡕࡧ࡯ࡆࡸࡧࡴ࠰ࡳࡹࡸ࡮ࠨࡳࡧࡶࡳࡱࡼࡥࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡾࡪࡳࡥࡢࡰࡦࡼࢁࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࡿࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯ࠨࡼࡣࡵ࡫ࡤࡰࡳࡰࡰࢀ࠭ࠧࠨࠢᅐ")
            bstack1llll111lll_opy_ = bstack1llll111lll_opy_.replace(bstack1ll1l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅑ"), bstack1ll1l_opy_ (u"ࠥࡦࡸࡺࡡࡤ࡭ࡖࡨࡰࡇࡲࡨࡵࠥᅒ"))
            script = bstack1llll111l1l_opy_.format(fn_body=bstack1llll111lll_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠦࡦ࠷࠱ࡺࡡࡶࡧࡷ࡯ࡰࡵࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡊࡸࡲࡰࡴࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡥ࠶࠷ࡹࠡࡵࡦࡶ࡮ࡶࡴ࠭ࠢࠥᅓ") + str(e) + bstack1ll1l_opy_ (u"ࠧࠨᅔ"))